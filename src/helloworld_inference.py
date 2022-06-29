import os
import sys
import json
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
        with open('model_json.txt','r') as file:
            model_param = json.load(file)

        MilesPredicted = model_param['intercept'] + model_param['coef'][0]*self.Usage + model_param['coef'][1]*self.Fitness
        return MilesPredicted