from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import os

app = Flask(__name__)

# Initialize the model variable
model = None

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload_dataset', methods=['POST'])
def upload_dataset():
    global model
    file = request.files['dataset']
    
    if file and file.filename.endswith('.csv'):
        # Save the uploaded file
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Load the dataset
        df = pd.read_csv(filepath)

        # Check if required columns exist
        required_columns = ['Temperature', 'Pulse', 'Disease']
        if not all(col in df.columns for col in required_columns):
            return render_template('upload.html', message="Please upload a correct CSV file with 'Temperature', 'Pulse', and 'Disease' columns.")

        # Features and labels
        X = df[['Temperature', 'Pulse']]
        y = df['Disease']

        # Train a Decision Tree Classifier
        model = DecisionTreeClassifier()
        model.fit(X, y)

        return render_template('upload.html', message="Dataset uploaded and model trained successfully!")
    else:
        return render_template('upload.html', message="Invalid file format. Please upload a CSV file.")

@app.route('/predict_disease', methods=['POST'])
def predict_disease_route():
    global model
    if model is None:
        return render_template('results.html', predicted_disease="Model not trained. Please upload a dataset first.", precautions="")

    temperature_str = request.form.get('temperature')
    pulse_str = request.form.get('pulse')

    # Validate and convert input to float
    try:
        temperature = float(temperature_str)
        pulse = float(pulse_str)
    except ValueError:
        return render_template('results.html', predicted_disease="Invalid input", precautions="Please enter valid numbers for temperature and pulse.")

    # Use the trained model to make a prediction
    predicted_disease = model.predict([[temperature, pulse]])[0]

    # Generate precaution message based on predicted disease
    precaution_message = generate_precaution_message(predicted_disease)

    # Render the results on the results.html page
    return render_template('results.html', predicted_disease=predicted_disease, precautions=precaution_message)

def generate_precaution_message(disease):
    """Generate precaution message based on the predicted disease."""
    precautions = {
        "Severe Heat Stress": "Immediate cooling measures required; consult a veterinarian.",
        "Moderate Heat Stress": "Monitor closely; provide shade and hydration.",
        "Mild Heat Stress": "Ensure hydration and rest in a cool area.",
        "Possible Viral Infection": "Monitor symptoms; consult a veterinarian if symptoms worsen.",
        "Bradycardia": "Monitor closely; consult a veterinarian if symptoms persist.",
        "Hypothermia": "Provide warmth and monitor closely; consult a veterinarian if symptoms persist.",
        "Possible Bacterial Infection": "Consult a veterinarian for further evaluation.",
        "Healthy": "No specific precautions needed.",
        "Hyperthermia": "Immediate cooling measures required; consult a veterinarian.",
        "Severe Hypothermia": "Immediate warming and veterinary assistance required.",
        "Severe Tachycardia": "Monitor closely; consult a veterinarian if symptoms persist.",
    }
    return precautions.get(disease, "Consult a veterinarian for further evaluation.")

if __name__ == '__main__':
    app.run(debug=True)