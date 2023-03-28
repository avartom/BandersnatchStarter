from base64 import b64decode
import os

# from Fortuna import random_int, random_float
# from MonsterLab import Monster
from flask import Flask, render_template, request
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder

from app.data import Database
from app.graph import chart
from app.machine import Machine

SPRINT = 3
APP = Flask(__name__)


@APP.route("/")
def home():
    return render_template("home.html",
        sprint=f"Sprint {SPRINT}",
        demographic = {'age':39, 'gender':"male",'bmi': 23.2 , 
                       'bloodpressure':91, 'diabetic':"Yes",'children':0, 
                       'smoker':'No','region':'southeast', 'claim':1121.87
                    },
        #monster=Monster().to_dict(),
        password=b64decode(b"VGFuZ2VyaW5lIERyZWFt"),)


@APP.route("/data")
def data():
    if SPRINT < 1:
        return render_template("data.html")
    db = Database('collection')
    return render_template(
        "data.html",
        count=db.count(),
        table=db.html_table(),
    )


@APP.route("/view", methods=["GET", "POST"])
def view():
    if SPRINT < 2:
        return render_template("view.html")
    db = Database('collection')
    options = ["age", "bmi", "bloodpressure", "gender", "claim", 
               "smoker", "children", "region", "diabetic"]
    x_axis = request.values.get("x_axis") or options[2]
    y_axis = request.values.get("y_axis") or options[4]
    target = request.values.get("target") or options[5]
    graph = chart(
        df=db.dataframe(),
        x=x_axis,
        y=y_axis,
        target=target,
    ).to_json()
    return render_template(
        "view.html",
        options=options,
        x_axis=x_axis,
        y_axis=y_axis,
        target=target,
        count=db.count(),
        graph=graph,
    )


@APP.route("/model", methods=["GET", "POST"])
def model():
    if SPRINT < 3:
        return render_template("model.html")
    db = Database('collection')
    options = [ "age","gender", "bmi", "bloodpressure", "diabetic",
                "children","smoker", "region", "claim"]
    filepath = os.path.join("app", "model.joblib")
    if not os.path.exists(filepath):
        df = db.dataframe()
        machine = Machine(df[options])
        machine.save(filepath)
    else:
        machine = Machine.open(filepath)
    Age = request.values.get("age", type=int) or 39
    Gender = request.values.get("gender", type=int) or 1
    BMI = request.values.get("bmi", type=float) or 23.2
    Bloodpressure = request.values.get("bloodpressure", type=int) or 91
    Diabetic = request.values.get("diabetic", type=int) or 1
    Children = request.values.get("children", type=int) or 0
    Smoker = request.values.get("smoker", type=int) or 0
    Region = request.values.get("region", type=int) or 3

    dframe = DataFrame([dict(zip(options, [Age, Gender, BMI, Bloodpressure, Diabetic, 
                        Children, Smoker, Region]))])
    prediction = machine.predict(dframe)
    # prediction = machine(DataFrame(
    #             [dict(zip(options, [Age, Gender, BMI, Bloodpressure, Diabetic, 
    #                         Children, Smoker, Region]))]
    # ))

 
    # info = machine.info()
    return render_template(
        "model.html",
        info= "Random Forest Classifier",
        Prediction=prediction,
        confidence=".94%",
    )


if __name__ == '__main__':
    APP.run()
