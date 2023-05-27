from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd
import cleaning as cl
import features_engineering as fe


# App definition
app = Flask(__name__)

# importing models
with open('model.p', 'rb') as f:
   model = pickle.load (f)

with open('columns.p', 'rb') as f:
   model_columns = pickle.load (f)

#webpage

@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Loan Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)

           query = pd.DataFrame(json_)
           query = query.reindex(columns = model_columns, fill_value= 0)
               
           prediction = list(model.predict(query))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })



if __name__ == "__main__":
   app.run()



