import pandas as pd
from tqdm import tqdm
import json

from eval.evaluation import Evaluator
from eval.connectors import Connector

class VQAV2Evaluator(Evaluator):
    """
    Queries the model server for answers.
    The questions are provided to the instance
    by the `data` argument, as a DataFrame
    with at least 3 columns equal to `question_id`, `question`, and `image_id`
    The directory to the images is provided by the `img_dir` parameter.
    """

    def __init__(self, data: pd.DataFrame, img_dir: str = 'datasets/VQA_V2/test2015'):
        self.data = data
        self.img_dir = img_dir

    def get_responses(self, out_path: str):
        if (self.connector == None):
            raise ValueError('No VLM connector provided. Call `Evaluator.connect()` to connect.')
        

        with open(out_path, 'a+', 1) as f_out, open(out_path + "_ERRORS", 'a+', 1) as error_out:
            try:
                answered_questions = pd.read_json(out_path, lines=True)['question_id'].unique()
            except:
                answered_questions = pd.Series()

            remaining_questions = self.data.loc[~self.data['question_id'].isin(answered_questions)]
            
            for img_id in tqdm(remaining_questions['image_id'].unique().astype(int)):
                img_path = f'{self.img_dir}/COCO_test2015_{img_id:012d}.jpg'
                
                for _, q in remaining_questions.loc[(remaining_questions['image_id'] == img_id)].iterrows():
                    try:
                        response = self.connector.completion(f'{q["question"]}', image_data=[{"id": int(img_id), "data": self.connector.encode64(img_path)}])

                        f_out.write(json.dumps({
                            "question_id": q["question_id"],
                            "response": response
                        }) + '\n')
                    except Exception as err:
                        error_out.write(json.dumps({
                            "question_id": q["question_id"],
                            "e": err
                        }) + '\n')