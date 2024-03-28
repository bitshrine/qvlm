from eval.connectors import Connector
import requests
import json

class LlamafileConnector(Connector):
    """
    Request different LLM tasks through llamafile
    """

    def __init__(self, url: str, port: int, prompt_format: str = 'USER: {prompt}\nASSISTANT:'):
        super().__init__('llamafile', url, port)

        if prompt_format == None or len(prompt_format) == 0:
            prompt_format = '{prompt}'

        self.prompt_format = prompt_format

    def completion(self, prompt: str, image_data: list[dict] = None, **kwargs) -> str:
        """
        ### Llamafile completion.

        The image is sent to the model through the `image_data` argument. Images
        must be passed as `{id: data}` dicts, where each `data` is the base64 string of image data.
        The images are then prepended to the prompt.
        """
        headers = {'Content-Type': 'application/json'}
        request = {
            "prompt": self.prompt_format.format(prompt=prompt)
        }

        if (kwargs != None):
            for arg in kwargs.keys():
                request.update({arg: kwargs[arg]})

        if (image_data != None and len(image_data) > 0):
            request['prompt'] = f'[img-{image_data['id']}]{request['prompt']}'
            request.update({"image_data": image_data})

        response = requests.post(f'http://{self.url}:{self.port}/completion',
                      headers = headers,
                      data = json.dumps(request)
                      )
        
        return json.loads(response.content)['content']
        
