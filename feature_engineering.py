import pandas as pd

# Load dataset
df = pd.read_csv("f1_strategy_2023.csv")

print("Original shape:", df.shape)

# Drop pit lap columns for v1 (keep it simple)
df = df.drop(columns=["First_Pit_Lap", "Second_Pit_Lap"])

# One-hot encode compounds
df = pd.get_dummies(df, columns=["First_Compound", "Second_Compound", "Third_Compound"])

# Encode driver + race as categorical
df = pd.get_dummies(df, columns=["Driver", "Race"])

print("After encoding shape:", df.shape)

df.to_csv("f1_strategy_features_2023.csv", index=False)

print("Feature dataset saved.")