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

    def completion(self, prompt: str, image_data: list = None, args: dict = None) -> str:
        """
        ### Llamafile completion.
        Images can be added to the prompt using "[img-<id>]" tokens, for example:
        ```text
        [img-1]USER: Describe this image in detail.\\nASSISTANT:
        ```
        The image is sent to the model through the `image_data` argument. Images
        must be passed as `{"id": id, "data": base64 string of image data}`
        """
        headers = {'Content-Type': 'application/json'}
        request = {
            "prompt": self.prompt_format.format(prompt=prompt)
        }

        if (args != None):
            for arg in args.keys():
                request.update({arg: args[arg]})

        if (image_data != None and len(image_data) > 0):
            request.update({"image_data": image_data})

        response = requests.post(f'http://{self.url}:{self.port}/completion',
                      headers = headers,
                      data = json.dumps(request)
                      )
        
        return json.loads(response.content)['content']
        
