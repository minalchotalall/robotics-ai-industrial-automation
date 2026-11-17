import pandas as pd
import numpy as np

print("======================================")
print(" ROBOT SENSOR DATA CLEANING")
print("======================================")

# 1. Create sensor data with missing and incorrect values
data = {
    "Temperature": [22, 25, np.nan, 32, 38, 150, 42, 45],
    "Pressure": [1.2, 1.4, 1.5, np.nan, 2.0, 2.1, 2.2, 2.4],
    "Speed": [100, 110, 120, 130, np.nan, 145, 150, 155]
}

df = pd.DataFrame(data)

print("\n--- ORIGINAL SENSOR DATA ---")
print(df)

# 2. Identify temperature outliers using IQR

Q1 = df["Temperature"].quantile(0.25)
Q3 = df["Temperature"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Temperature"] < lower_limit) |
    (df["Temperature"] > upper_limit)
]

print("\n--- TEMPERATURE OUTLIERS ---")
print(outliers)

print("Number of outliers:", len(outliers))

# 2. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 3. Replace missing values with column averages
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["Pressure"] = df["Pressure"].fillna(df["Pressure"].mean())
df["Speed"] = df["Speed"].fillna(df["Speed"].mean())

print("\n--- DATA AFTER FILLING MISSING VALUES ---")
print(df)

# 4. Identify incorrect temperatures
df.loc[df["Temperature"] > 100, "Temperature"] = np.nan

print("\n--- DATA AFTER REMOVING INVALID TEMPERATURES ---")
print(df)

# 5. Fill invalid temperatures with the average
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())

print("\n--- CLEANED SENSOR DATA ---")
print(df)

# 6. Calculate statistics
print("\n--- CLEANED DATA STATISTICS ---")
print(df.describe())

# 7. Normalize sensor data between 0 and 1

df_normalized = (
    (df - df.min()) /
    (df.max() - df.min())
)

print("\n--- NORMALIZED SENSOR DATA ---")
print(df_normalized)

# 8. Export cleaned data to CSV

df.to_csv("cleaned_sensor_data.csv", index=False)

print("\nCleaned sensor data exported successfully!")

print("\nExercise 04 completed!")
