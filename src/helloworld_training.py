import os
import sys
import argparse
import numpy as np
import pandas as pd
sys.path.append(".")
from modeltraining import ModelTraining
from os.path import isfile, join

class HelloWorldTraining(ModelTraining):

    def __init__(self):
        pass
        

    def train(self):
        
        try:
           # Load the Cardio Dataset
            mydata = pd.read_csv('CardioGoodFitness.csv')
               
        except Exception as e:
            raise e



def main():
    m = HelloWorldTraining()
    return m.train()


if __name__== "__main__":
    retval = main()
    print(f"End with ({retval})")