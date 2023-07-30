import pandas as pd
import joblib
import numpy as np
import os
import warnings 

warnings.filterwarnings("ignore")

# 과제 3. 현재 학습된 모델인 model.pkl을 app.py와 같은 경로에 저장하고 ml_model.py의 load_model() 함수에서 사용
def load_model():
    model_path = ?
    return ?

# 예측 결과 출력
def predict(input_values, model):
    return model.predict(np.array(input_values))