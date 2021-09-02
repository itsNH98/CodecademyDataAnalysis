import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())
print(diabetes_data.info())
print(diabetes_data.isnull().sum())
print(diabetes_data.describe())

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

print(diabetes_data.isnull().sum())
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
print(diabetes_data.dtypes)

diabetes_data["Outcome"] = diabetes_data.Outcome.str.replace('O', '0')
diabetes_data["Outcome"] = pd.to_numeric(diabetes_data.Outcome)
print(diabetes_data.Outcome.unique())