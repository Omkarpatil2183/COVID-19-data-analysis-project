import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('covid_data.csv')

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Handle missing values
data['Recovered'].fillna(0, inplace=True)

data['Date'] = pd.to_datetime(data['Date'])

print("\nMissing Values:")
print(data.isnull().sum())

print("\nSummary Statistics:")
print(data.describe())

data['Active'] = data['Confirmed'] - (data['Recovered'] + data['Deceased'])

data.to_csv('cleaned_covid_data.csv', index=False)
print("\nCleaned dataset saved as cleaned_covid_data.csv")

# Visualization: Confirmed Cases Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='Confirmed', label='Confirmed')
plt.title('Confirmed Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.show()

# Visualization: Active Cases Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='Active', label='Active Cases', color='orange')
plt.title('Active Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Active Cases')
plt.legend()
plt.grid(True)
plt.show()

# Visualization: Recovered and Deceased Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='Recovered', label='Recovered', color='green')
sns.lineplot(data=data, x='Date', y='Deceased', label='Deceased', color='red')
plt.title('Recovered and Deceased Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.show()
