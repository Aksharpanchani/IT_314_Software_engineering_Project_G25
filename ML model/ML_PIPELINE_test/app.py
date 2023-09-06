from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        HighBP = 1 if request.form.get('HighBP') else 0
        HighChol = 1 if request.form.get('HighChol') else 0
        HeartDiseaseorAttack = 1 if request.form.get('HeartDiseaseorAttack') else 0

        BMI = float(request.form['BMI'])
        Income = float(request.form['Income'])
        GenHlth = float(request.form['GenHlth'])
        Age = float(request.form['Age'])

        # Prepare input data
        data = [HighBP, HighChol, BMI, Income, HeartDiseaseorAttack, GenHlth, Age]

        # Predict
        prediction = model.predict([data])[0]

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
