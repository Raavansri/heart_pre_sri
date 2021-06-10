from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('heart_atack_pre.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict ():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=prediction*100
    return render_template('home.html',prediction_text='There is {}% chance of attack'.format(output))

if __name__ =='__main__':
    app.run(debug=True)
