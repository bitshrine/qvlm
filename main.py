from eval.connectors.llamafile import LlamafileConnector

if __name__ == "__main__":
    
    connector = LlamafileConnector('localhost', 8080, 'USER:{prompt}\nAnswer using a single word or phrase.\nASSISTANT:')
    
    response = connector.completion('[img-1] Who is the person in the image?',
                        image_data=[{"id": 1, "data": connector.encode64('img/beyonce.jpeg')}]
                        #args={"n_predict": 10}
                        )
    
    print(response)