import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
column_name=["id","area","bedrooms","month_sold","year_sold","sale_price"]
balance_data = pd.read_csv('train.csv', names=column_name, header=0)


column_name_test=["id","area","bedrooms","month_sold","year_sold"]
test_dataset = pd.read_csv('test.csv', names=column_name_test, header=0)
test_x = test_dataset.iloc[:, 1:5].values

	
print( "Dataset Lenght:: ", len(balance_data))
print( "Dataset Shape:: ", balance_data.shape)


print ("Dataset:: ")
balance_data.head()


X = balance_data.values[:, 1:5]
Y = balance_data.values[:,5]


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0, random_state = 100)



clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=5, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)

y_pred_en = clf_entropy.predict(test_x)
print(y_pred_en.tolist())
#print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)



