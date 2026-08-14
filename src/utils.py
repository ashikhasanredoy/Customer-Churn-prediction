import os
import pickle
import dill
import sys
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import recall_score

from src.exception import CustomException

def save_object_file(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)   

def model_evaluate(X_train, y_train, X_test, y_test, models, param):
    try:
        report={}
        
        for model_name,model in models.items():
            params=param[model_name]
            rando_search=RandomizedSearchCV(model,params,cv=5)
            rando_search.fit(X_train,y_train)
            model.set_params(**rando_search.best_params_)
            model.fit(X_train,y_train)
            y_test_predict=model.predict(X_test)
            test_recall=recall_score(y_test,y_test_predict,average='weighted',zero_division=0)
            
            report[model_name]=test_recall
            print(f"The {model_name}: Recall = {test_recall:.4f}")
        
        return report    
    
    except Exception as e:
        raise CustomException(e,sys)                 

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            try:
                return dill.load(file_obj)
            except Exception:
                file_obj.seek(0)
                return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)                     