import pandas as pd
from tqdm import tqdm
import json

from eval.evaluation import Evaluator

class SEED1Evaluator(Evaluator):
    """
    Queries the model server for answers.
    The questions are provided to the instance
    by the "data" argument.
    This implementation uses GBNF grammars to force the model to output one of the multiple choices
    from the SEED benchmark, as outlined by the [SEED evaluation specification](https://github.com/AILab-CVC/SEED-Bench/blob/main/EVALUATION.md)
    
    > [...] for each choice of a question, we compute the likelihood that a model generates the content of this choice given the question. We select the choice with the highest likelihood as model's prediction. Our evaluation strategy does not rely on the instruction-following capabilities of models to output 'A' or 'B' or 'C' or 'D'.
    """

    def __init__(self, data: pd.DataFrame, img_dir: str = 'datasets/SEED/SEED-Bench-image'):
        self.data = data
        self.img_dir = img_dir

    def get_responses(self, out_path: str):
        if (self.connector == None):
            raise ValueError('No VLM connector provided. Call `Evaluator.connect()` to connect.')
        
        with open(out_path, 'a+', 1) as f_out, open(out_path + "_ERRORS", 'a+', 1) as error_out:
            try:
                answered_questions = pd.read_json(out_path, lines=True)['question_id'].astype(int).unique()
            except:
                answered_questions = pd.Series()
            
            remaining_questions = self.data.loc[~self.data['question_id'].astype(int).isin(answered_questions)]

            for data_id in tqdm(remaining_questions['data_id'].unique()):
                img_path = f'{self.img_dir}/{data_id}'
                
                for _, q in remaining_questions.loc[(remaining_questions['data_id'] == data_id)].iterrows():
                    try:
                        response = self.connector.completion(f'{q["question"]}',
                                                             image_data=[{"id": int(data_id), "data": self.connector.encode64(img_path)}],
                                                             grammar_string=self._generate_grammar_for_question(q))
                        
                        if (response == q['choice_a']):
                            prediction = 'A'
                        elif (response == q['choice_b']):
                            prediction = 'B'
                        elif (response == q['choice_c']):
                            prediction = 'C'
                        elif (response == q['choice_d']):
                            prediction = 'D'
                        else:
                            raise ValueError(f'Response "{response}" was not among possible choices.')

                        f_out.write(json.dumps({
                            "question_id": q["question_id"],
                            "prediction": prediction
                        }) + '\n')
                    except Exception as err:
                        error_out.write(json.dumps({
                            "question_id": q["question_id"],
                            "e": str(err)
                        }) + '\n')

    def eval(self, answer_path: str) -> float:
        answers_df = pd.read_json(open(answer_path), lines=True, dtype=str)
        merged_df = pd.merge(answers_df, self.data, how='left', left_on='question_id', right_on='question_id')
        accuracy = (len(merged_df.loc[merged_df['prediction'] == merged_df['answer']]) / len(merged_df)) * 100.0
        print(f"""
    Total accuracy on SEED-Bench: {accuracy:.2f}
""")
        return accuracy

    def _generate_grammar_for_question(self, row: pd.Series) -> str:
        """
        Generate a grammar string to constrain the model's output
        possibilities.
        The grammar has the following form:
        ```
        root ::= <choice A> | <choice B> | <choice C> | <choice D>
        ```
        """
        ca = row['choice_a']
        cb = row['choice_b']
        cc = row['choice_c']
        cd = row['choice_d']
        return f'''root ::= ("{ca}" | "{cb}" | "{cc}" | "{cd}")'''