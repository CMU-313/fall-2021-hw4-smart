from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 # parse entries from the input
     studytime = request.args.get('studytime', type=int)
     failures = request.args.get('failures', type=int)
     schoolsup = request.args.get('schoolsup', type=int)
     famsup = request.args.get('famsup', type=int)
     activities = request.args.get('activities', type=int)
     freetime = request.args.get('freetime', type=int)
     higher = request.args.get('higher', type=int)
     Dalc = request.args.get('Dalc', type=int)
     Walc = request.args.get('Walc', type=int)
     internet = request.args.get('internet', type=int)
     health = request.args.get('health', type=int)
     absences = request.args.get('absences', type=int)

     # produce dataframe
     query_df = pd.DataFrame({ 'studytime' : pd.Series(studytime),
                                'failures' : pd.Series(failures),
                                'schoolsup' : pd.Series(schoolsup), 
                                'famsup' : pd.Series(famsup),
                                'activities' : pd.Series(activities),
                                'higher' : pd.Series(higher),
                                'internet' : pd.Series(internet),
                                'freetime' : pd.Series(freetime), 
                                'Dalc' : pd.Series(Dalc),
                                'Walc' : pd.Series(Walc), 
                                'health' : pd.Series(health),
                                'absences' : pd.Series(absences),
                                })
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)

     # return prediction
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model_new.pkl')
    app.run(host="0.0.0.0", debug=True)