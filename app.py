import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import random
import pickle


 

app = Flask(__name__) #Initialize the flask App


model = pickle.load(open('soft.pkl', 'rb'))
@app.route('/')
@app.route('/')
@app.route('/index') 
def index():
	return render_template('index.html')
@app.route('/login') 
def login():
	return render_template('login.html')    
@app.route('/chart') 
def chart():
	return render_template('')    
@app.route('/abstract') 
def abstract():
	return render_template('abstract.html')    
@app.route('/performance') 
def  performance():
	return render_template('')   
@app.route('/future') 
def future():
	return render_template('')  
@app.route('/upload') 
def upload():
	return render_template('upload.html') 
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('loc', inplace=True)
        return render_template("preview.html",df_view = df)    

 
@app.route('/home')



def home():
    return render_template('test.html')

  


@app.route('/predict',methods=['POST'])
def predict():
    
    
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
        
    prediction = model.predict(final_features)
    output = prediction
    prediction = 1
    final_output = print(random.randint(0,1))
    
    print(output)
    return render_template('test.html', prediction_text= output)
  
    
    
if __name__ == "__main__":
    app.run(debug=True)
