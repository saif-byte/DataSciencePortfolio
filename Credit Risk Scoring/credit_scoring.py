import pickle
import numpy as np
import xgboost as xgb
from flask import Flask, request , jsonify

def predict_single(person , dv , model):
  X = dv.transform(person)
  dX = xgb.DMatrix(X , feature_names = dv.feature_names_)
  y_pred = model.predict(dX)
  return y_pred

with open('credit_model.bin' ,'rb') as f_in:
  dv,model = pickle.load(f_in)
app = Flask('credit_scoring')

@app.route('/predict' , methods = ["POST"])
def predict():
  person = request.get_json()
  prediction = predict_single(person , dv,model)
  default = prediction>=0.5
  result={
    'default probablity' : float(prediction),
    'default': bool(default)
  }
  return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True , host = '0.0.0.0' , port = 9696)

