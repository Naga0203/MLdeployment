MLdeployment

Project Overview

MLdeployment is a Django-based web application designed to deploy a machine learning model for predicting heart disease. The project involves data preprocessing, model training, evaluation, and deployment using Django and Render.

Dataset

The model is trained on the heart_disease_dataset, which contains health-related attributes that help in predicting the presence of heart disease. The dataset includes features such as:

Age

Sex

Blood Pressure

Cholesterol Levels

Resting ECG Results

Maximum Heart Rate Achieved

ST Depression

And other clinical attributes

Model Building

Data Preprocessing:

Handling missing values

Normalization and scaling

Feature selection

Model Training:

Machine Learning Algorithms Explored:

XGBoost

LightGBM (LGBM)

Random Forest

Gradient Boosting

The best-performing model, XGBoost, was selected based on evaluation metrics like accuracy, precision, recall, and F1-score.

Evaluation:

Model performance was assessed using test data.

Confusion matrix and ROC-AUC curves were used to analyze classification effectiveness.

Deployment

Backend Framework: Django

Frontend: HTML, CSS

Hosting: Render

Prediction Handling: The HDmodel app handles user inputs and predictions using the get_predictions function.

Templates:

index.html: Accepts user input

result.html: Displays prediction results

Future Improvements

Enhance the model using deep learning techniques.

Improve the UI for a better user experience.

Deploy on additional cloud platforms for scalability.

Contributors:

Naga Durgarao Thuttupu - Developer & ML Engineer
