import os

import mlflow.sklearn
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import RandomForestClassifier

from utils import utils
from pipeline.utils import load_data

class rfc_model:
    '''
    Random Forest Classifier model to predict crypto pump and dump schemes
    '''

    def __init__(self,
        dataset_id='newest',
        data_root='data/engineered/',
        **cv_params):
        '''
        Constructor
        :param model_params: cross validation parameters (key-value-pair) for the model
        '''
        self.data = load_data(dataset_id,data_root=data_root)
        self.params = cv_params
