# 🐄 Cattle Health Analysis — ML Web App

A machine learning web application that predicts cattle diseases based on **body temperature** and **pulse rate** using a Decision Tree Classifier. Built with Flask and scikit-learn.

---

## 📌 Features

- Upload a CSV dataset to train the ML model
- Predict cattle disease based on temperature and pulse input
- Displays precautionary measures for the predicted disease
- Simple and clean web interface

---

## 🧠 Machine Learning

- **Algorithm:** Decision Tree Classifier (scikit-learn)
- **Input Features:** Temperature, Pulse
- **Output:** Predicted Disease + Precaution Message

### Diseases Detected
| Disease | Precaution |
|---|---|
| Severe Heat Stress | Immediate cooling; consult a vet |
| Moderate Heat Stress | Provide shade and hydration |
| Mild Heat Stress | Rest in a cool area |
| Possible Viral Infection | Monitor; consult vet if worsens |
| Bradycardia | Monitor; consult vet if persists |
| Hypothermia / Severe Hypothermia | Provide warmth; immediate vet help |
| Possible Bacterial Infection | Consult a veterinarian |
| Hyperthermia | Immediate cooling required |
| Severe Tachycardia | Monitor closely |
| Healthy | No precautions needed |

---

## 🗂️ Project Structure

```
cattle-health-analysis-ml/
│
├── app.py                  # Main Flask application
├── run.bat                 # Windows batch file to start the app
├── requirements.txt        # Python dependencies
│
├── templates/
│   ├── upload.html         # Upload dataset & input page
│   └── results.html        # Prediction results page
│
├── data sets/
│   ├── sample_data.csv
│   ├── sample_data_1000.csv
│   └── sample_data_2000.csv
│
└── uploads/                # Uploaded files (auto-created)
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cattle-health-analysis-ml.git
cd cattle-health-analysis-ml
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```
Or on Windows, double-click `run.bat`

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 📊 Dataset Format

Your CSV file must contain these columns:

| Column | Description | Example |
|---|---|---|
| `Temperature` | Body temperature of cattle (°F) | 102.5 |
| `Pulse` | Pulse rate (beats/min) | 70 |
| `Disease` | Disease label | Healthy |

Sample datasets are provided in the `data sets/` folder.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn (Decision Tree Classifier)
- **Data Processing:** pandas
- **Frontend:** HTML, Jinja2 Templates

---

## 👤 Author

> Developed as a livestock health monitoring ML project.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
