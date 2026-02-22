# 🏎 F1 Tyre Strategy Prediction System

An end-to-end machine learning pipeline for predicting Formula 1 race strategies and first pit stop timing using real historical race data.

This project extracts race data using FastF1, engineers meaningful race features, trains classification and regression models, and evaluates strategy prediction performance.

---

## 🚀 Project Goals

The objective of this project is to:

- Predict the number of pit stops in a race (classification)
- Predict the first pit stop lap (regression)
- Build a scalable dataset across multiple F1 seasons
- Simulate real-world race strategy modeling logic

This system is designed to be extended into a race simulator and deployed via Flask in future iterations.

---

## 📊 Data Source

Data is extracted using:

- FastF1 Python library
- Official Formula 1 timing data

The system automatically builds structured race datasets across seasons.

---

## 🧠 Features Used

For each driver and race:

- Grid Percentile (starting position normalized)
- Track Temperature (average)
- Air Temperature (average)
- Total Race Laps
- Safety Car Lap Count
- First Tyre Compound
- Tyre Degradation Rate (first stint)

---

## 🤖 Models

### 1️⃣ Stop Prediction (Classification)
- Model: RandomForestClassifier
- Target: Number of pit stops
- Handles class imbalance using `class_weight="balanced"`

### 2️⃣ First Pit Stop Prediction (Regression)
- Model: RandomForestRegressor
- Target: First pit stop lap
- Evaluated using MAE and R²

---

## 📈 Current Performance (2023 Season)

Stop Prediction Accuracy: ~85%  
First Pit Stop MAE: ~5.5 laps  
R² Score: ~0.56  

Performance improves as more seasons are added.

---

## 📁 Project Structure
f1_strategy/
│
├── build_dataset.py # Builds multi-race dataset
├── feature_engineering.py # Prepares ML-ready features
├── train_model.py # Stop prediction model
├── train_pit_model.py # Pit lap regression model
├── f1_strategy_2023.csv
├── requirements.txt
└── README.md


---

## 🔥 Future Improvements

- Add multi-season training (2019–2024)
- Include track characteristics (street vs permanent)
- Model safety car probability
- Build Monte Carlo race simulation
- Deploy via Flask as interactive strategy tool
- Explore XGBoost / LightGBM for improved accuracy

---

## 🛠 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/f1_strategy.git

cd f1_strategy

Install dependencies:


pip install -r requirements.txt


Run dataset builder:


python build_dataset.py


Train models:


python train_model.py
python train_pit_model.py


---

## 🏁 Long-Term Vision

This project aims to evolve into a full F1 race simulation engine capable of:

- Strategy optimization
- Real-time race modeling
- Scenario testing (1-stop vs 2-stop vs undercut)
- Reinforcement learning-based decision systems

---

## 📌 Disclaimer

This project is for educational and research purposes only and is not affiliated with Formula 1, FIA, or any team.