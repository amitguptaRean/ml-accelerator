from abc import ABC, abstractmethod

class ModelInference(ABC):
    """
    Model inferencing that takes json input and returns json output
    """
    @abstractmethod
    def run(self, *, json_input):
        pass
