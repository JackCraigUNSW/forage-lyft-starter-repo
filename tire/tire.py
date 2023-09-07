from abc import ABC, abstractmethod



class Tires(ABC):
    def __init__(self, wear):
        self.wear = wear

    @abstractmethod
    def needs_service(self):
        pass