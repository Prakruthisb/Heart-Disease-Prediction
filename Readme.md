# ❤️ Heart Disease Prediction using Machine Learning

## Project Overview
This project aims to predict whether a patient has heart disease based on various clinical parameters. By leveraging machine learning algorithms, the model analyzes patterns in medical data to assist in early diagnosis and decision-making.

## Problem Statement
Given a set of clinical features of a patient, the goal is to predict the presence of heart disease.
- Input: Patient health parameters
- Output:
    - 0 → No Heart Disease
    - 1 → Heart Disease Present

## Objectives

- Perform Exploratory Data Analysis (EDA) to understand the dataset
- Build and compare multiple machine learning models
- Optimize model performance using hyperparameter tuning
- Achieve high prediction accuracy (target: ~95%)

## Dataset

- Dataset contains 303 samples and 14 features
- Includes attributes such as:
    - Age
    - Sex
    - Chest pain type (cp)
    - Resting blood pressure
    - Cholesterol levels
    - Maximum heart rate (thalach)
    - And more...

## 📂 Data Source:
[Heart Disease Dataset](https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv)

## Exploratory Data Analysis (EDA)

EDA was performed to understand:
- Distribution of features
- Class balance of target variable
- Relationships between features

Key Insights:
- Target variable is almost balanced
- Certain features like chest pain type and max heart rate show strong correlation with heart disease
- Visualization techniques used:
    - Bar plots
    - Scatter plots
    - Histograms
    - Crosstab analysis

## Technologies Used

- Programming Language: Python 🐍
- Libraries:
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Scikit-learn

## Machine Learning Models Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Random Forest Classifier

## Model Training & Evaluation

- Data split into training and testing sets
- Models evaluated using:
    - Accuracy
    - Precision
    - Recall
    - F1-score
    - Confusion Matrix
- Cross-validation used for better generalization

## Hyperparameter Tuning

- RandomizedSearchCV
- GridSearchCV
Used to optimize model performance and select the best parameters.

## 📈 Results

- Achieved strong performance across multiple models
- Random Forest and Logistic Regression performed particularly well
- Model successfully captures patterns in patient health data

## 📊 Visualizations

Some important visualizations include:
![Heart Disease Frequency vs Sex](plots/Heart%20Disease%20Frequency%20vs%20Sex.png)
![Age vs Maximum Heart Rate](plots/Age%20vs%20Maximum%20Heart%20Rate.png)
![Heart Disease vs Chest Pain Type](plots/Heart%20Disease%20vs%20Chest%20Pain%20Type.png)
![Feature importance](plots/Features%20Importance.png)

## Key Learnings

- Importance of EDA in understanding data
- Feature relationships significantly impact model performance
- Hyperparameter tuning improves accuracy
- Visualization helps in identifying patterns and trends

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the notebook:
```bash
jupyter notebook
```

## Future Improvements

- Use advanced models like XGBoost or Neural Networks
- Add real-time prediction interface
- Improve accuracy with feature engineering

## 👩‍💻 Author

Prakruthi S B

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐
It helps others discover the project.