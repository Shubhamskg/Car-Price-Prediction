from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Location=request.form['location']
        Year = int(request.form['year'])
        Kilometers_Driven=int(request.form['Kilometers'])
        Fuel_Type=request.form['fuel']
        Transmission=request.form['Transmission']
        Owner_Type=int(request.form['Owner'])
        Mileage=float(request.form['mileage'])
        Engine=float(request.form['engine'])
        Power=float(request.form['power'])
        Seats=int(request.form['seats'])
        Company=request.form['company']
        Model=request.form['model']

        prediction=model.predict(pd.DataFrame([[Location,Year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats,Company,Model]],
                                              columns=['Location', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Mileage', 'Engine', 'Power', 'Seats', 'Company', 'Model']))
        output=prediction[0]
        print(output)
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {} Lakhs INR".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

