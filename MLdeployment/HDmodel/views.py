from django.shortcuts import render, redirect
from django.http import JsonResponse
import numpy as np
from joblib import load
from sklearn.preprocessing import StandardScaler
import pickle

with open('savedmodels/model.pkl','rb') as file:
    model = pickle.load(file)

with open('savedmodels/scaler.pkl','rb') as file1:
    scaler = pickle.load(file1)

def pred(request):
    return render(request, 'index.html')

def get_predictions(request):
    result = None 
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        pain_type = request.POST.get('pain-type')
        bp = request.POST.get('bp')
        cholesterol = request.POST.get('cholesterol')
        fbs = request.POST.get('fbs')
        ecg = request.POST.get('ecg')
        max_hr = request.POST.get('max_hr')
        exercise = request.POST.get('exercise')
        depression = request.POST.get('depression')
        slope = request.POST.get('slope')
        vessels = request.POST.get('vessels')
        thal = request.POST.get('thal')
        history = request.POST.get('history')
        smoking = request.POST.get('smoking')
        alcohol = request.POST.get('alcohol')
        activity = request.POST.get('activity')
        medication = request.POST.get('medication')
        gender = int(1 if gender == 'Male' else 0)
        new_data = np.array([[age, gender, pain_type, bp, cholesterol, fbs, ecg,
                              max_hr, exercise, depression, slope, vessels, thal, history,
                              smoking, alcohol, activity, medication]])
        
        new_data = scaler.transform(new_data)
        prediction = model.predict(new_data)
        probability = model.predict_proba(new_data)[0, 1]
        
        mes = "Your health is quite good" if prediction == 0 else "You have to be careful about your Health"
        
        result = {
            'prediction': int(prediction[0]),
            'probability': probability,
            'message': mes
        }
        
        
        return render(request, 'result.html', {'result': result})
    
    

