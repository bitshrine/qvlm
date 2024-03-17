from abc import ABC
from eval.connectors import Connector

class Evaluator(ABC):

    def __init__(self):
        pass

    def connect(self, connector: Connector):
        self.connector = connector

    def get_responses(self, out_path: str):
        pass

    def eval(self, answer_path: str):
        pass


    