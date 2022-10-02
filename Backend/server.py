from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from joblib import load
import numpy as np
import pickle
import json

X_Address = load('X_Address.joblib')
clf = load("Ethereum_Fraud_Detection.joblib")

# Initializing flask app
app = Flask(__name__)
CORS(app) 


# with open('model_pickle', 'rb') as f:
#     clf =pickle.load(f)
        
# with open('X_Address_pickle', 'rb') as f:
#     X_Address =pickle.load(f)
  
@app.route('/predict', methods=["POST"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])

def prediction_func():
        data = request.json
        temp = X_Address.where(X_Address['Address'] == "0x00009277775ac7d0d59eaad8fee3d10ac6c805e8")
        X_info = temp.dropna().iloc[:,0:44]
        print(X_info)
        prediction = clf.predict(X_info)
        response = jsonify({"result": "The Prediction is: "+ prediction[0]})
        return response         
    
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)