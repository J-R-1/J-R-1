from flask import Flask, redirect, url_for, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.svm import SVC

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        p_name = request.form['name']
        p_title = request.form['Title']
        p_gender = request.form['gender']
        p_age = int(request.form['age'])
        p_isalone = request.form['isalone']
        p_passclass = request.form['pass_class']
        p_fare = int(request.form['fare'])
        p_pol = request.form['port']

        # Title :
        t_val = 0
        if p_title == 'Mr':
            t_val = 1
        elif p_title == 'Miss':
            t_val = 2
        elif p_title == 'Mrs':
            t_val = 3
        elif p_title == 'Master':
            t_val = 4
        else:
            t_val = 5

        title = t_val

        # Gender :
        if p_gender == 'Male':
            male = 0
            female = 1
        else:
            male = 1
            female = 0

        # Age :
        if p_age <= 16:
            age = 0
        elif (p_age > 16) & (p_age <= 32):
            age = 1
        elif (p_age > 32) & (p_age <= 48):
            age = 2
        elif (p_age > 48) & (p_age <= 64):
            age = 3
        else:
            age = 4

        # IsAlone :
        isalone = 0 if p_isalone == 'No' else 1

        # Passenger Class :
        f_class, s_class, t_class = 0, 0, 0
        if p_passclass == "First Class":
            f_class = 1
        elif p_passclass == "Second Class":
            s_class = 1
        else:
            t_class = 1

        # Fare :
        if p_fare <= 7.91:
            fare = 0
        elif (p_fare > 7.91) & (p_fare <= 14.454):
            fare = 1
        elif (p_fare > 14.454) & (p_fare <= 31):
            fare = 2
        else:
            fare = 3

        # Port of Leaving :
        e_c, e_q, e_s = 0, 0, 0
        if p_pol == "C":
            e_c = 1
        elif p_pol == "Q":
            e_q = 1
        else:
            e_s = 1

        # User Input Function
        def user_input_features():
            data = {
                'Age': age,
                'Fare': fare,
                'IsAlone': isalone,
                'Title': title,
                'Pclass 1': f_class,
                'Pclass 2': s_class,
                'Pclass 3': t_class,
                'Male': male,
                'Female': female,
                'E_C': e_c,
                'E_Q': e_q,
                'E_S': e_s
            }
            features = pd.DataFrame(data, index=[0]).fillna(0)
            return features

        df = user_input_features()

        model = pickle.load(open('svc_pkl.pkl', 'rb'))
        prediction = model.predict(df.values)
        predict_probability = model.predict_proba(df.values)

        if prediction[0] == 1:
            result = ('Passenger {}.{} would have survived with a probability of {}%'.format(p_title, p_name, round(predict_probability[0][1]*100, 2)))
            return render_template('predict.html', prediction=result)
        else:
            result = ('Passenger {}.{} would not have survived with a probability of {}%'.format(p_title, p_name, round(predict_probability[0][0]*100, 2)))
            return render_template('predict.html', prediction=result)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)


