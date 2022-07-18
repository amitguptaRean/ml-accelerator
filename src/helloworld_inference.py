import os
import sys
import json
import argparse
import numpy as np
import pandas as pd
sys.path.append(".")
from modelinference import ModelInference
from os.path import isfile, join
import pickle

class HelloWorldInference(ModelInference):

    def __init__(self, Usage, Fitness):
        self.Usage = Usage
        self.Fitness = Fitness

        print("usage:", self.Usage, "; fitness:", self.Fitness)

        pass
        
    """
    return MilesPredicted
    """
    def run(self):
        # load and evaluate the model
        ##   from JSON
        #with open('model_json.txt','r') as file:
        #    model_param = json.load(file)
        #
        #print(model_param)
        # 
        #MilesPredicted = model_param['intercept'] + model_param['coef'][0]*self.Usage + model_param['coef'][1]*self.Fitness
        #print(MilesPredicted)

        
        filename = 'model_pickle.sav'
        model_param = pickle.load(open(filename, 'rb'))

        print(model_param)

        MilesPredicted = model_param.predict(np.array([[self.Usage, self.Fitness]]))[0]
        print(MilesPredicted)

        return MilesPredicted
    
def main():
    m = HelloWorldInference(1, 2)
    #print(m)

    return m.run()


if __name__== "__main__":
    retval = main()
    print(f"End with ({retval})")