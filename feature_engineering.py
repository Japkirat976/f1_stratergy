import pandas as pd

df = pd.read_csv("f1_strategy_2023.csv")

# Drop missing rows
df = df.dropna()

# One-hot encode compound
df = pd.get_dummies(df, columns=["First_Compound"])

df.to_csv("f1_strategy_features_2023.csv", index=False)

print("Feature dataset saved.")