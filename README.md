# Crop Recommendation System

A machine learning-based web application that recommends suitable crops based on soil and environmental conditions.

## Project Overview

This project uses machine learning classification models to recommend a crop based on seven input parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

The project uses an agricultural dataset containing 2,200 records covering 22 crop classes.

## Machine Learning Models

Three classification models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Model Performance

| Model | Test Accuracy |
|---|---:|
| Logistic Regression | 97.05% |
| Decision Tree | 99.55% |
| Random Forest | 99.77% |

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Flask
- Joblib

## Project Workflow

1. Load and inspect the agricultural dataset.
2. Perform data validation and exploratory analysis.
3. Separate input features and target labels.
4. Split the dataset into training and testing sets.
5. Train multiple classification models.
6. Compare model performance using test accuracy.
7. Save the trained model.
8. Integrate the trained model with a Flask web application.
9. Accept soil and environmental parameters through a web form.
10. Return the predicted crop recommendation.

## Flask Web Application

The Flask application provides a web interface where users enter the seven soil and environmental parameters. The trained machine learning model processes these values and returns the predicted crop.

## Dataset

The dataset contains 2,200 records across 22 crop classes with the following input features:

`N, P, K, temperature, humidity, ph, rainfall`

## How to Run

### 1. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib flask joblib

### 2. Run the Flask application

```bash
python crop_app.py
```

### 3. Open the application

Open the local Flask URL shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## Project Structure

```text
Crop-Recommendation-System/
│
├── crop_app.py
├── module_name.py
├── crop_app1
├── Crop_recommendation.csv
├── Untitled.ipynb
└── templates/
    ├── Home_1.html
    ├── index.html
    └── prediction.html
```

## Future Improvements

- Add more agricultural and regional datasets.
- Evaluate models using additional performance metrics.
- Add visual analytics for soil and weather conditions.
- Deploy the application to a cloud platform.
  ```
  ## Author

**Onkar**

GitHub: https://github.com/Onkar142
