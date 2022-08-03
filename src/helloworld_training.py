import os
import json
import sys
import argparse
import numpy as np
import pandas as pd
from modeltraining import ModelTraining
from sklearn.model_selection import cross_val_score
from os.path import isfile, join
from sklearn import linear_model

import pickle

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

            # Use k-fold cross-validation to properly assess model quality
            scores = -1 * cross_val_score(regr,x,y,cv = 5,scoring='neg_root_mean_squared_error')
            print(scores.mean())

            # Train the model using the training sets
            regr.fit(x,y)  

            # save model
            #   as JSON
            model_param = {}
            model_param['coef'] = list(regr.coef_)
            model_param['intercept'] = regr.intercept_.tolist()

            model_json = json.dumps(model_param, indent = 4)
            with open('model_json.txt','w') as file:
                file.write(model_json)
            
            #   as pickle
            filename = 'cardio_fitnesss_model.pkl'
            pickle.dump(regr, open(filename, 'wb'))
            print('Helloworld - Cardio Fitness Model training completed')

        except Exception as e:
            raise e



def main():
    m = HelloWorldTraining()
    return m.train()


if __name__== "__main__":
    retval = main()
    print(f"End with ({retval})")