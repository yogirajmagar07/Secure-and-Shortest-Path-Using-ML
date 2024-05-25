import os
import sys
from dataclasses import dataclass

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            
            from sklearn.neighbors import KNeighborsClassifier
            # instantiate the model
            knn = KNeighborsClassifier(n_neighbors=3)


            save_object(
               file_path=self.model_trainer_config.trained_model_file_path,
               obj=knn
            )
            knn.fit(X_train, y_train)

            predicted=knn.predict(X_test)

            

            accuracy=accuracy_score(y_test,predicted)
            return accuracy
            



            
        except Exception as e:
            raise CustomException(e,sys)