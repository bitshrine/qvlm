import pandas as pd
from tqdm import tqdm

from eval.evaluation import Evaluator
from eval.connectors import Connector

class VQAV2Evaluator(Evaluator):

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def compute(self, out_path: str):
        if (self.connector == None):
            raise ValueError('No VLM connector provided. Call `Evaluator.connect()` to connect.')
        

        with open(out_path, 'w+') as f_out:
            for img_id in tqdm(self.data['image_id'].unique().astype(int)):
                img_path = f'datasets/VQA_V2/test2015/COCO_test2015_{img_id:012d}.jpg'
                #self.connector.completion(f'[img-{img_id}]')
                
                for _, q in self.data.loc[self.data['image_id'] == img_id].iterrows():
                    response = self.connector.completion(f'[img-{img_id}]{q['question_id']}', image_data=[{"id": int(img_id), "data": self.connector.encode64(img_path)}])

                    f_out.write(f'{{"question_id": {q['question_id']},  "response": "{response}"}},\n')