from abc import ABC, abstractmethod

class ModelTraining(ABC):
    @abstractmethod
    def train(self):
        pass
