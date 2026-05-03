import os
import pickle
import dill
import sys

from src.exception import CustomException

def save_object_file(file_path,obj):
    try:
        dir_path=os.path.join(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)        