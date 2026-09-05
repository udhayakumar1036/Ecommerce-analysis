import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("online+retail/Online Retail.xlsx")

print("Dataset loaded successfully!")
print("Original Shape:", df.shape)

df = df.drop_duplicates()

df = df.dropna(subset=["CustomerID"])

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]


df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]


df = df.reset_index(drop=True)

print("\nData cleaning completed!")
print("Cleaned Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())