import os
import sys
import argparse
import numpy as np
import pandas as pd
sys.path.append(".")
from modeltraining import ModelTraining
from os.path import isfile, join

class HelloWorldInference(ModelTraining):

    def __init__(self):
        # load the model
        pass
        

    def run(self):
        # MilesPredicted = -56.74 + 20.21*Usage + 27.20*Fitness
        return -1