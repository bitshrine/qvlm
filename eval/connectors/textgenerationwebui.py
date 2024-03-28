import json, re
import requests

from eval.connectors import Connector

class TextGenerationWebUIConnector(Connector):
    """
    Send requests to a running `text-generation-webui` server.
    The server must have been started with the `--api` argument.
    Note that the multimodal extension is still bugged, so
    the server should NOT be started with the `--no-web-ui` argument
    as it relies on some UI code to process images.
    """

    def __init__(self, url: str, port: int, prompt_format: str = '{prompt}'):
        super().__init__('textgenerationwebui', url, port)
        self.prompt_format = prompt_format


    def completion(self, prompt: str, image_data: list = [], **kwargs) -> str:
        """
        ### TextGenerationWebUI completion.

        The image is sent to the model through the `image_data` argument.
        Note that only a single image will be sent per message.


        This implementation uses the /v1/chat/completions endpoint of the API.
        """
        headers = {'Content-Type': 'application/json'}

        request = {
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{self.prompt_format.format(prompt=prompt)}"
                    }
                    ]
                }
            ]
        }

        for img in image_data:
            request['messages'][-1]['content'].append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img['data']}"}})

        if (kwargs != None):
            for arg in kwargs.keys():
                request.update({arg: kwargs[arg]})

        response = requests.post(f'http://{self.url}:{self.port}/v1/chat/completions',
                      headers = headers,
                      json = request
                      )
        
        return json.loads(response.content)['choices'][-1]['message']['content']