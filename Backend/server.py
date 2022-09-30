from flask import Flask
from flask_cors import CORS
  
# Initializing flask app
app = Flask(__name__)
CORS(app) 
  
# Route for seeing a data
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    return {
        "Output": "This Address seems Fraudulent"
        }
  
@app.route('/add', methods=["POST"])
def addingAddress():
    return "done", 201
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)