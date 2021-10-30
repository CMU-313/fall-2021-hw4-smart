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
	 #use entries from the query string here but could also use json
     studytime = request.args.get('studytime')
     failures = request.args.get('failures')
     schoolsup = request.args.get('schoolsup')
     famsup = request.args.get('famsup')
     activities = request.args.get('activities')
     freetime = request.args.get('freetime')
     higher = request.args.get('higher')
     Dalc = request.args.get('Dalc')
     Walc = request.args.get('Walc')
     internet = request.args.get('internet')
     health = request.args.get('health')
     absences = request.args.get('absences')
     data = [[studytime],[failures],[schoolsup],[famsup],[activities],[freetime],[higher],
            [Dalc],[Walc],[internet],[health],[absences]]
     query_df = pd.DataFrame({ 'studytime' : pd.Series(studytime),
                                'failures' : pd.Series(failures),
                                'schoolsup' : pd.Series(schoolsup), 
                                'famsup' : pd.Series(famsup),
                                'activities' : pd.Series(activities),
                                'freetime' : pd.Series(freetime), 
                                'higher' : pd.Series(higher),
                                'Dalc' : pd.Series(Dalc),
                                'Walc' : pd.Series(Walc), 
                                'internet' : pd.Series(internet),
                                'health' : pd.Series(health),
                                'absences' : pd.Series(absences), })
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model_new.pkl')
    app.run(host="0.0.0.0", debug=True)