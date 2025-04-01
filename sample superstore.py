import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file_path = r"C:\\Users\\jahna\\OneDrive\\Desktop\\Data analysis\\Sample - Superstore Original Data (1).csv"
# 🔹 Check if the file exists
if not os.path.isfile(file_path):
    print(f" Error: The file does not exist at:\n{file_path}")
    print(" Double-check the file path and ensure the file is not open in another program.")
    exit()

print(" File exists and is accessible.")

#  Try loading the dataset
try:
    # Load the CSV file (since your uploaded file is CSV, not Excel)
    df = pd.read_csv(file_path, encoding="utf-8")

    print("\n Dataset loaded successfully!\n")
    print(df.head())  # Display first few rows
except UnicodeDecodeError:
    print("\n UnicodeDecodeError: Trying a different encoding (ISO-8859-1)...")
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print("\n Dataset loaded successfully with ISO-8859-1 encoding!\n")
        print(df.head())
    except Exception as e:
        print(f"\n Failed to load the dataset: {e}")
        exit()
except Exception as e:
    print(f"\n Error loading the dataset: {e}")
    exit()

    # Check for missing values
missing_values = df.isna().sum()
print("\nMissing Values in Dataset:\n", missing_values)

# Data information
print("\nDataset Info:\n")
df.info()
# Correlation heatmap
plt.figure(figsize=(8, 5))
numeric_data = df.select_dtypes(include=['number'])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Matrix")
plt.show()

df.groupby("City")["Profit"].sum().sort_values().plot(kind="bar", color="skyblue", figsize=(12, 6))

plt.xlabel("City")
plt.ylabel("Total Profit")
plt.title("City-wise Profit Distribution")
plt.xticks(rotation=90)
plt.show()

# Violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x="Category", y="Profit", data=df)
plt.title("Violin Plot of Profit by Category")
plt.show()

# Box Plot for Numerical Features
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, palette='Set2')
plt.title("Boxplot of Features")
plt.show()