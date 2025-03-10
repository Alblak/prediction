from flask import Flask, request, render_template

app=Flask(__name__)

import joblib

model_Random_Fores=joblib.load("model_Random_Fores.pkl")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    import numpy as np
    features=[float(i) for i in request.form.values()]
    mesfeatures=np.array(features).reshape(1,-1)
    prediction=model_Random_Fores.predict(mesfeatures)
    resultat="OUI" if prediction[0]==1 else "NON"
    return render_template("index.html", resultat=f" presence de complicatation : {resultat}")
if __name__=="__main__":
    app.run(debug=True)
