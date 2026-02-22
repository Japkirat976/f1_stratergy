import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load ORIGINAL dataset (not encoded one)
df = pd.read_csv("f1_strategy_2023.csv")

# Drop missing values
df = df.dropna()

# One-hot encode compound
df = pd.get_dummies(df, columns=["First_Compound"])

# Define features
X = df.drop(columns=["Num_Stops", "First_Pit_Lap", "Year", "Round"])
y = df["First_Pit_Lap"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))