import json
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__) #here we are creating a basic flask application, here __name__ will be the starting point of our application.
model = pickle.load(open('modl.pkl','rb')) #loading the model 
scalar = pickle.load(open('scaling.pkl','rb'))
#Here this declares the first route and this basically take us to the homepage
@app.route('/')
def home():
    return render_template('home.html')

#here we are routing to a prediction api and POST is used to give a post request because from our side we are going to give some input and that will capture the input and will give that to our model and will there by give use the output 
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data'] 
#When we hit predict_api, the input we are gonna give, we are going to make sure that we are taking json file which is captured inside the data key
#we will take this data and transform this into a pickle file.then standardize this data and then send this to the model
    print(data)
    print(np.array(list(data.values())).reshape(1,-1)) #we are using np inorder to reshape the array so that the transformed data can be fed to the model for predictions
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    return jsonify(output[0])
@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()] #When we specifically write this,whatever values we fill in the form we will be able to capture it because all the information will be present in this request object and we use float to convert everything into float
    final_input = scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The house price prediction is {}".format(output))
    
if __name__ == "__main__":
    app.run(debug=True)