# -*- coding: utf-8 -*-
"""Untitled89.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KdhabxVzOVyivRdUGKzCQKAOd9sJk96L
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load your tire quality data into a Pandas DataFrame
df = pd.read_csv('tire_quality_data.csv')

# Basic summary statistics
summary_stats = df.describe()

# Histogram of tread wear
plt.hist(df['tread_wear'], bins=20, edgecolor='k')
plt.xlabel('Tread Wear')
plt.ylabel('Frequency')
plt.title('Distribution of Tread Wear')
plt.show()

# Scatter plot of tire pressure vs. fuel efficiency
plt.scatter(df['tire_pressure'], df['fuel_efficiency'])
plt.xlabel('Tire Pressure (psi)')
plt.ylabel('Fuel Efficiency (mpg)')
plt.title('Tire Pressure vs. Fuel Efficiency')
plt.show()