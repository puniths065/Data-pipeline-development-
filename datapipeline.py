import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("student_data.csv")

print("Original Data:")
print(data)

# Select only numeric columns
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# Create Data Pipeline
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),   # Handle missing values
    ("scaler", StandardScaler())                   # Feature scaling
])

# Apply pipeline
prepared_data = pipeline.fit_transform(numeric_data)

# Convert back to DataFrame
prepared_df = pd.DataFrame(prepared_data, columns=numeric_data.columns)

print("\nPrepared Data:")
print(prepared_df)

# Save processed data
prepared_df.to_csv("prepared_data.csv", index=False)

print("\nData Pipeline Completed Successfully")
