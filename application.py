from flask import Flask, request, render_template
import os
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load scaler
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")
scaler = pickle.load(open(scaler_path, "rb"))

# Load model
model_path = os.path.join(BASE_DIR, "models", "heart_disease_model.pkl")
model = pickle.load(open(model_path, "rb"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == "POST":
        try:
            Age = float(request.form.get("Age"))
            Sex = float(request.form.get("Sex"))
            Chest_pain_type = float(request.form.get("Chest_pain_type"))
            BP = float(request.form.get("BP"))
            Cholesterol = float(request.form.get("Cholesterol"))
            FBS_over_120 = float(request.form.get("FBS_over_120"))
            EKG_results = float(request.form.get("EKG_results"))
            Max_HR = float(request.form.get("Max_HR"))
            Exercise_angina = float(request.form.get("Exercise_angina"))
            ST_depression = float(request.form.get("ST_depression"))
            Slope_of_ST = float(request.form.get("Slope_of_ST"))
            Number_of_vessels_fluro = float(request.form.get("Number_of_vessels_fluro"))
            Thallium = float(request.form.get("Thallium"))

            # Create input array
            data = np.array([[Age, Sex, Chest_pain_type, BP, Cholesterol,
                              FBS_over_120, EKG_results, Max_HR,
                              Exercise_angina, ST_depression,
                              Slope_of_ST, Number_of_vessels_fluro,
                              Thallium]])

            # Scale data
            scaled_data = scaler.transform(data)

            # Predict
            prediction = model.predict(scaled_data)[0]

            if prediction == 1:
                result = "⚠ Person HAS Heart Disease"
            else:
                result = "✅ Person does NOT have Heart Disease"

            return render_template("home.html", result=result)

        except Exception as e:
            return render_template("home.html", result="Error: Please enter valid values.")

    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
