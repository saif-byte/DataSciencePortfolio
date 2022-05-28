import pickle 
import numpy as np
from flask import Flask , jsonify , request
def predict_single(customer, dv, model):
  X = dv.transform([customer])
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]
#now we will load our model
with open('churn-model.bin' ,'rb') as f_in:
  dv,model = pickle.load(f_in)

app = Flask('churn')
@app.route('/predict' , methods = ["POST"])
def predict():
  customer = request.get_json()
  prediction = predict_single(customer , dv , model)
  churn  = prediction>=0.5
  result = {
    'churn probablity' : float(prediction),
    'churn': bool(churn)

  }
  return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True , host = '0.0.0.0' , port = 9696)
  
