from abc import ABC
import base64

class Connector(ABC):
    """
    Abstract class to process different LLM requests
    """

    def __init__(self, name: str, url: str, port: int = 8080):
        self.url = url
        self.port = port

    def completion(self, data: str, image_data: list, args: dict) -> str:
        """
        Request text completion from a model.
        Image data can be provided.
        Returns the model's text output.
        """
        pass

    def encode64(self, path: str) -> str:
        """
        Encode image data in b64 format
        """
        image_data: bytes = None
        with open(path, 'rb') as img:
            image_data = base64.b64encode(img.read())

        return image_data.decode()
