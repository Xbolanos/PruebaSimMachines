import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

# Define Colums name
column_name=["id","area","bedrooms","month_sold","year_sold","sale_price"]
# Read train.csv
balance_data = pd.read_csv('train.csv', names=column_name, header=0)

# Define Colums name
column_name_test=["id","area","bedrooms","month_sold","year_sold"]
# Read test.csv
test_dataset = pd.read_csv('test.csv', names=column_name_test, header=0)
test_x = test_dataset.iloc[:, 1:5].values
	

balance_data.head()

# Define Samples Attributes 
X = balance_data.values[:, 1:5]
# Define Samples Results
Y = balance_data.values[:,5]

# Set train and test data fro accuracy
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.5, random_state = 100)


# Create Decision Tree
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=4)
# Fit Model 
clf_entropy.fit(X_train, y_train)
# Predict for accuracy 
y_pred_en = clf_entropy.predict(X_test)
# Get Accuracy
print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)


# Calculate Predictions
pred_en = clf_entropy.predict(test_x)
# Save results in .csv	
results=np.concatenate((test_x, np.array([pred_en]).T), axis=1)
df = pd.DataFrame(results)
df.to_csv("decision-tree-results.csv")