import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df = pd.read_csv ('E:\Book1.csv')
x1=np.array(df['Height']).reshape(-1,1)
x2=np.array(df['Weight']).reshape(-1,1)
height = df[['Height','Weight']]
gender = df['Gender']



heightTrain, heightTest, genderTrain, gendertest = train_test_split(height, gender, test_size = 1/3, random_state = 0)

LogisticRegressor = LogisticRegression()

LogisticRegressor.fit(heightTrain, genderTrain)

genderprediction = LogisticRegressor.predict(heightTest)
print (genderprediction)
print ("accuracy is", LogisticRegressor.score(heightTest,gendertest))
plt.figure()
plt.scatter(heightTest[gendertest == 1].Weight, heightTest[gendertest == 1].Height, color = 'blue', label = 'Male')
plt.scatter(heightTest[gendertest == 0].Weight, heightTest[gendertest == 0].Height, color = 'red', label = 'Female')
plt.show()
