from flask import Flask, render_template, request
import os
from ml_model import load_model, predict
import config

app = Flask(__name__)
app.config.from_object(config)

# 과제1. '/'에 접속하면 바로 form.html에 접속하도록 경로 설정 
def home():    
    # 과제 2. foms.py에 작성된 form을 활용하여 데이터를 한번에 입력받을 수 있도록 활용

    if form.validate_on_submit():
        age = form.age.data
        bmi = form.bmi.data
        children = form.children.data
        smoker = form.smoker.data
        sex = form.sex.data
        region = form.region.data

        model = load_model()
        input_values = [[age, bmi, children, smoker, sex == "남성", region == "북서", region == "북동", region == "남서"]]
        prediction = predict(input_values, model)

        return render_template('result.html', prediction=prediction[0])

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)