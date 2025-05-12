# COVID-19 Global Data Tracker - Python Script Version

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Load the dataset (Make sure the CSV is in the same directory or update the path)
try:
    df = pd.read_csv("owid-covid-data.csv")  # Replace with your CSV file if different
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()

# Display basic info
df.info()
print("\nPreview of dataset:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Data Cleaning
# Focus on selected countries
countries = ["United States", "India", "Kenya", "Brazil", "United Kingdom"]
df = df[df['location'].isin(countries)]

# Drop rows with missing date or critical values
df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])
df['date'] = pd.to_datetime(df['date'])

# Fill missing numeric values with forward fill
df.fillna(method='ffill', inplace=True)

# Exploratory Data Analysis
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Daily new cases comparison
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'].fillna(0), label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate death rate = total_deaths / total_cases
df['death_rate'] = df['total_deaths'] / df['total_cases']

# Vaccination Progress
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'].fillna(method='ffill'), label=country)
plt.title('Total COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Insights
print("\nKey Insights:")
print("1. The USA has had the highest number of reported cases and deaths over time.")
print("2. India showed a rapid rise in cases during its second wave.")
print("3. Kenya had comparatively lower total cases but showed consistent growth.")
print("4. Vaccination rollout was faster in developed countries like the UK and USA.")
print("5. Death rates vary significantly, showing better healthcare outcomes in some regions.")
