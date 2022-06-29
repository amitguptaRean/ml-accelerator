import os
import sys
import argparse
import numpy as np
import pandas as pd
sys.path.append(".")
from modeltraining import ModelTraining
from os.path import isfile, join

class HelloWorldInference(ModelTraining):

    def __init__(self, Usage, Fitness):
        self.Usage = Usage
        self.Fitness = Fitness
        pass
        
    """
    return MilesPredicted
    """
    def run(self):
        # load the model
        MilesPredicted = -56.74 + 20.21*self.Usage + 27.20*self.Fitness
        return MilesPredicted