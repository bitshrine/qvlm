from eval.connectors.llamafile import LlamafileConnector
from eval.connectors.textgenerationwebui import TextGenerationWebUIConnector
import json
import pandas as pd
    
from eval.evaluation.VQAV2 import VQAV2Evaluator

if __name__ == "__main__":
    
    #connector = LlamafileConnector('localhost', 8080, 'USER:{prompt}\nAnswer using a single word or phrase.\nASSISTANT:')
    connector = TextGenerationWebUIConnector('localhost', 5000, '{prompt}\nAnswer using a single word or phrase.')
    #response = connector.completion('[img-1] Who is the person in the image?',
    #                    image_data=[{"id": 1, "data": connector.encode64('img/beyonce.jpeg')}]
    #                    #args={"n_predict": 10}
    #                    )

    questions_json = json.load(open('datasets/VQA_V2/v2_Questions_Test_mscoco/v2_OpenEnded_mscoco_test-dev2015_questions.json'))
    questions_df = pd.DataFrame(questions_json['questions'])

    evaluator = VQAV2Evaluator(questions_df.head(10))
    evaluator.connect(connector)

    evaluator.compute('datasets/VQA_V2/llava1.5_17B_responses.jsonl')