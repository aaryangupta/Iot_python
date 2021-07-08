import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix


x1 = np.array([2.327868056, 3.032830419, 4.485465382, 3.684815246, 2.283558563, 7.807521179, 6.132998106, 7.514829366, 5.502385039, 7.43293235])
x2 = np.array([2.458016525, 3.170770366, 3.696728111, 3.846846973, 1.853215097, 3.290132136, 2.140563087, 2.107056961, 1.404002608, 4.236232628])
y = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])

x = np.column_stack((x1, x2))

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = .50)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(x)
print(y_pred)
print(svclassifier.score(x,y))



#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))

