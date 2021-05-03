import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier


from sklearn.metrics import classification_report, confusion_matrix


path = open("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\dateSortie.csv")

# Assign colum names to the dataset
namesTest= ['_id', 'humidity', 'date', 'pressure', 'temperature', 'light', 'rain']
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
dataset = pd.read_csv(path, names=namesTest)


x = dataset.iloc[:,:-1].values
y =  dataset.iloc[:,4].values



X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

print(X_test[0])

scaler = StandardScaler()
scaler.fit(X_train)


X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)





classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)



y_pred = classifier.predict([X_test])



'''
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


dataset.head()'''