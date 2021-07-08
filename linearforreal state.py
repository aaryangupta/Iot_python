import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("Linear regression model using scikit_learn on house price")

#Read the data from csv file.

df= pd.read_csv('E:\Real estate.csv')

x1 = np.array(df['X1 transaction date']).reshape(-1, 1)
x2 = np.array(df['X2 house age']).reshape(-1, 1)
x3 = np.array(df['X3 distance to the nearest MRT station']).reshape(-1, 1)
x4 = np.array(df['X4 number of convenience stores']).reshape(-1, 1)
x5 = np.array(df['X5 latitude']).reshape(-1, 1)
x6 = np.array(df['X6 longitude']).reshape(-1, 1)
x = df[['X1 transaction date', 'X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores', 'X5 latitude', 'X6 longitude',]]
y = df['Y house price of unit area']


X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=1)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("intercept", regressor.intercept_)

y_pred = regressor.predict(X_test)
print (X_test,y_pred)

print ("Accuracy is the model of:", regressor.score(X_test,y_test))

#plt.figure()
#plt.scatter(X_test[y_test == 1].Weight, X_test[y_test == 1].Height, color = 'blue', label = 'Male')
#plt.scatter(X_test[y_test == 0].Weight, X_test[y_test == 0].Height, color = 'red', label = 'Female')
#plt.show()
