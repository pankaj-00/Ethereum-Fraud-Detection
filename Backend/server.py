from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from joblib import load
import numpy as np



# Initializing flask app
app = Flask(__name__)
CORS(app) 


X_Address = load('X_Address.joblib')
clf = load("Ethereum_Fraud_Detection.joblib")
  
@app.route('/predict', methods=["POST"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])

#Sample Address = 0x00009277775ac7d0d59eaad8fee3d10ac6c805e8

def prediction_func():
        data = request.json
        temp = X_Address.where(X_Address['Address'] == data[1:-1])
        X_info = temp.dropna().iloc[:,0:44]
        # print(X_info) #get information related to that data point 
        prediction = clf.predict_proba(X_info)
        response = jsonify({"result": "The Prediction is: "+ str(prediction[0][0])})
        return response         
    
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)