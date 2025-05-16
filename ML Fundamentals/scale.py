# For now there's errors due to 'Organisation Id,' a column of unique values. That's understandable
# Use a dataset that has more numerical values which are typical in nature

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv('ML Fundamentals\organizations-100.csv')
X = df[['Organization Id', 'Number of employees', 'Index']] 
y = df['Founded']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

model = LinearRegression

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
print(f'mean squared error: {mse}')


