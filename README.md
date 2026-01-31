# Heart Disease Prediction

A web-based application that predicts whether a person has heart disease based on clinical parameters. Built using **Python**, **Flask**, and **machine learning**.

---

## Features

- Predicts the likelihood of heart disease using user inputs.
- Interactive web interface built with Flask.
- Clean and responsive design for easy use.
- Categorical fields use dropdowns to prevent invalid inputs.
- Shows color-coded prediction results (red = heart disease, green = no heart disease).

---

## Input Parameters

The application takes the following inputs:

| Parameter                  | Type         | Notes                                           |
|-----------------------------|--------------|------------------------------------------------|
| Age                         | Number       | Age of the patient                             |
| Sex                         | Select       | 0 = Female, 1 = Male                           |
| Chest Pain Type             | Select       | 0-3 (typical/atypical/non-anginal/asymptomatic) |
| Resting Blood Pressure (BP) | Number       | Measured in mmHg                               |
| Cholesterol                 | Number       | Serum cholesterol in mg/dl                     |
| FBS over 120                | Select       | 0 = No, 1 = Yes                                |
| EKG Results                 | Select       | 0-2 (Normal/ST-T Abnormality/LVH)            |
| Max Heart Rate              | Number       | Maximum heart rate achieved                    |
| Exercise Angina             | Select       | 0 = No, 1 = Yes                                |
| ST Depression               | Number       | Measured in mm                                 |
| Slope of ST                 | Select       | 0-2 (Upsloping/Flat/Downsloping)             |
| Number of Vessels Fluoro    | Select       | 0-3 major vessels                               |
| Thallium Test               | Select       | 1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect |

---

## Technologies Used

- **Python 3**
- **Flask** (Web framework)
- **Scikit-learn** (Machine Learning model)
- **NumPy** (Numerical operations)
- **HTML/CSS** (Frontend)
- **Pickle** (Model serialization)

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/vedddev/Heart-Diesese-Predication.git
cd Heart-Diesese-Predication
