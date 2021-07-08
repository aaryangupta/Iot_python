import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv ('E:\iris.csv')
x1=np.array(df['Length'])
x2=np.array(df['Width'])
y = df['class']
x = np.column_stack((x1, x2))

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.40)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)
print(y_pred)
print(svclassifier.score(x,y))

#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))



