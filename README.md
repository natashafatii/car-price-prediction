# Car Price Prediction System 🚗💰

## Overview
This project implements a **Machine Learning-based Car Price Prediction System**. Users can predict the resale price of used cars based on key features including brand, model year, engine size, mileage, fuel type, transmission, and previous owners.

The system includes:
- Data preprocessing (handling missing values, encoding, scaling)
- Exploratory Data Analysis (EDA) with visualizations
- Regression models (Linear Regression & Random Forest) with evaluation metrics
- A live web interface using **Gradio**
- Deployment on **Hugging Face Spaces** for interactive usage

---

## Features
- Handle both **numerical and categorical variables**.
- Predict prices using trained ML models.
- Evaluate models with **R², MAE, MSE, and RMSE**.
- Save and reuse models, encoders, and scalers.
- Live interactive UI for predicting prices without coding.

---

## 📊 Dataset
**Dataset:** `car_price_dataset.csv`  
**Features:** 
- **Categorical:** Brand, Fuel Type, Transmission
- **Numerical:** Model Year, Engine Size, Mileage, Owner Count
- **Target:** Price (Rs)

---
## 🛠️ Tech Stack
- **Programming:** Python 3.9+
- **Libraries:** 
  - Data Processing: Pandas, NumPy
  - Visualization: Matplotlib, Seaborn
  - Machine Learning: Scikit-learn
  - Model Persistence: Joblib
  - Web Interface: Gradio
- **Deployment:** Hugging Face Spaces

---
## How to Use
1. Clone this repository:
```bash
git clone https://github.com/natashafatii/car-price-prediction.git
cd car-price-prediction
2. Install required packages:
```bash
pip install -r requirements.txt
3. Run the Gradio app:
```bash
python app.py
4. Input car details in the interactive UI and get predicted selling price.
## Models
- **Linear Regression**
- **Random Forest Regressor**

Trained models, encoders, and scalers are saved as `.pkl` files:
- `lr_model.pkl`
- `rf_model.pkl`
- `encoder.pkl`
- `scaler.pkl`

---

## Live Deployment
The app is deployed on **Hugging Face Spaces**.

- **Live App:** [Car Price Prediction](https://Natashaa0-car-price.hf.space)  
- **Source Code on Hugging Face:** [Repo Link](https://huggingface.co/spaces/Natashaa0/car-price/tree/main)

