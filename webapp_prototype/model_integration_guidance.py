# Dear Team,

# I hope this message finds you well. I wanted to inform you that I’m currently en route to Bristol and may not be able to join the activity before 4 PM today.

# Before heading out, I wrote a proof-of-concept demo for:

#   Model Integration - Priority prediction logic connected to Flask workflows

#   Rendering Logic - Dynamic case prioritization (Red > Amber > Green) with DB integration

# I’ve included documentation about:

#   Feature preprocessing requirements

#   Fallback mechanisms for model errors

#   Priority escalation rules

# You can modify it to adjust your new ideas. 

# Wishing you a smooth day ahead!

# Best regards,

# Tian

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import joblib  # Added for model loading
import numpy as np
from datetime import datetime

# --- Load ML Model and Preprocessing Objects ---
try:
    model = joblib.load('trained_model.pkl')
    encoder = joblib.load('label_encoder.pkl')
    scaler = joblib.load('scaler.pkl')
    feature_columns = joblib.load('feature_columns.pkl')  # Saved list of expected columns
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# --- Database Model ---
class Case(db.Model):  # I am used to use class generate table, you can change to your familiar way of doing it
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    epilepsy = db.Column(db.Boolean, default=False)
    historical_heart_attack_stroke = db.Column(db.Boolean, default=False)
    diabetes = db.Column(db.Boolean, default=False)
    mental_health = db.Column(db.Boolean, default=False)
    bmi = db.Column(db.Float)
    time_since_requested = db.Column(db.Integer)
    estimated_duration = db.Column(db.Float)
    critical_result = db.Column(db.Boolean, default=False)
    medication = db.Column(db.String(50))
    days_until_out = db.Column(db.Integer)
    polypharmacy = db.Column(db.Boolean, default=False)
    request_type = db.Column(db.String(50))
    monitoring_required = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# --- Helper Functions ---
def preprocess_input(form_data):
    """Replicate training preprocessing pipeline"""
    # Convert to DataFrame
    df = pd.DataFrame([form_data])
    
    # Convert booleans to integers
    bool_cols = ['epilepsy', 'historical_heart_attack_stroke', 
                'diabetes', 'mental_health', 'critical_result',
                'polypharmacy', 'monitoring_required']
    df[bool_cols] = df[bool_cols].astype(int)
    
    # Handle categorical features
    categoricals = {
        'task': ["prescription request", "patient communication (via phone, NHS app, AccuRX)",
                "sick notes", "referral letters", "medical reports", "review results"],
        'medication': medication_types['high'] + medication_types['medium'] + medication_types['low'],
        'request_type': request_types['high'] + request_types['medium'] + request_types['low']
    }
    
    # One-hot encode categoricals
    for col, categories in categoricals.items():
        for category in categories:
            df[f'{col}_{category}'] = (df[col] == category).astype(int)
        df.drop(col, axis=1, inplace=True)
    
    # Add missing columns with 0 values
    missing_cols = set(feature_columns) - set(df.columns)
    for col in missing_cols:
        df[col] = 0
    
    # Ensure correct column order
    df = df[feature_columns]
    
    # Scale numerical features
    numericals = ['bmi', 'time_since_requested', 'estimated_duration', 'days_until_out']
    df[numericals] = scaler.transform(df[numericals])
    
    return df

# --- Routes ---
@app.route('/') # change to your setting
def case_list():
    # Get cases ordered by priority (red first, then amber, then green)
    cases = Case.query.all()
    
    # Custom sorting logic
    priority_order = {'red': 0, 'amber': 1, 'green': 2}
    sorted_cases = sorted(cases, key=lambda x: priority_order[x.priority])
    
    return render_template('case_list.html', cases=sorted_cases)



@app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    if request.method == 'POST':
        # Collect form data
        form_data = {
            'task': request.form['task'],
            'epilepsy': int('epilepsy' in request.form),
            'historical_heart_attack_stroke': int('historical_heart_attack_stroke' in request.form),
            'diabetes': int('diabetes' in request.form),
            'mental_health': int('mental_health' in request.form),
            'bmi': float(request.form.get('bmi', 25.0)),
            'time_since_requested': int(request.form.get('time_since_requested', 0)),
            'estimated_duration': float(request.form.get('estimated_duration', 30.0)),
            'critical_result': int('critical_result' in request.form),
            'medication': request.form.get('medication', 'none'),
            'days_until_out': int(request.form.get('days_until_out', 0)) if request.form.get('days_until_out') else 0,
            'polypharmacy': int('polypharmacy' in request.form),
            'request_type': request.form.get('request_type', 'routine scheduled repeat'),
            'monitoring_required': int('monitoring_required' in request.form)
        }
        
        # Handle non-prescription cases
        if form_data['task'] != 'prescription request':
            form_data.update({
                'medication': 'none',
                'days_until_out': 0,
                'polypharmacy': 0,
                'request_type': 'none',
                'monitoring_required': 0
            })
        
        try:
            # Preprocess input
            processed_df = preprocess_input(form_data)
            
            # Make prediction
            prediction = model.predict(processed_df)
            priority = encoder.inverse_transform(prediction)[0]
        except Exception as e:
            # Fallback to rule-based system if model fails
            print(f"Model failed: {e}, using rule-based fallback")
            priority = assign_priority_with_uncertainty(
                task=form_data['task'],
                comorbidities=form_data,
                time_since_requested=form_data['time_since_requested'],
                critical_result=form_data['critical_result']
            )
        
        # Create and save new case
        new_case = Case(
            task=form_data['task'],
            epilepsy=form_data['epilepsy'],
            historical_heart_attack_stroke=form_data['historical_heart_attack_stroke'],
            diabetes=form_data['diabetes'],
            mental_health=form_data['mental_health'],
            bmi=form_data['bmi'],
            time_since_requested=form_data['time_since_requested'],
            estimated_duration=form_data['estimated_duration'],
            critical_result=form_data['critical_result'],
            medication=form_data['medication'] if form_data['task'] == 'prescription request' else None,
            days_until_out=form_data['days_until_out'] if form_data['task'] == 'prescription request' else None,
            polypharmacy=form_data['polypharmacy'],
            request_type=form_data['request_type'] if form_data['task'] == 'prescription request' else None,
            monitoring_required=form_data['monitoring_required'],
            priority=priority
        )
        
        db.session.add(new_case)
        db.session.commit()
        
        return redirect(url_for('case_list'))
    
    return render_template('add_case.html',
                          task_types=task_types,
                          comorbidities=comorbidities,
                          medication_types=medication_types,
                          request_types=request_types)
