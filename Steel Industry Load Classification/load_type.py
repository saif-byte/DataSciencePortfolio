import numpy as np
import pickle
from flask import Flask, request , jsonify

def predict_single(att , dv , model):
  X = dv.transform(att)
  y_pred = model.predict(X)
  return y_pred[0]

with open('load_type.bin' ,'rb') as f_in:
  dv,model = pickle.load(f_in)
app = Flask('load_type')

@app.route('/predict' , methods = ["POST"])
def predict():
  att = request.get_json()
  prediction = predict_single(att , dv,model)
  result={
    'load_type': prediction
  }
  return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True , host = '0.0.0.0' , port = 9696)