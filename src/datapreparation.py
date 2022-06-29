from abc import ABC, abstractmethod

class DataPreparation(ABC):
    @abstractmethod
    def preprocess(self):
        pass
