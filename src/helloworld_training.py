import os
import json
import sys
import argparse
import numpy as np
import pandas as pd
sys.path.append(".")
from modeltraining import ModelTraining
from os.path import isfile, join
from sklearn import linear_model

class HelloWorldTraining(ModelTraining):

    def __init__(self):
        pass
        

    def train(self):
        
        try:
            
            # Load the Cardio Dataset
            mydata = pd.read_csv('src/CardioGoodFitness.csv')
            # Simple Linear Regression

            #Load function from sklearn
            
            # Create linear regression object
            regr = linear_model.LinearRegression()

            y = mydata['Miles']
            x = mydata[['Usage','Fitness']]

            # Train the model using the training sets
            regr.fit(x,y)  
            model_param = {}
            model_param['coef'] = list(regr.coef_)
            model_param['intercept'] = regr.intercept_.tolist()
            model_json = json.dumps(model_param, indent = 4)
            with open('model_json.txt','w') as file:
                file.write('model_json')
                
        except Exception as e:
            raise e



def main():
    m = HelloWorldTraining()
    return m.train()


if __name__== "__main__":
    retval = main()
    print(f"End with ({retval})")