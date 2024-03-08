from abc import ABC, abstractmethod

class Server(ABC):
    """
    Abstract class to represent a server capable
    of handling requests.
    """

    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass