# Import Librarys 
from keras.models import Sequential
from keras.layers import Dense
import numpy
from numpy import genfromtxt
from keras.utils import np_utils
import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split

# Import train.csv
column_name=["id","area","bedrooms","month_sold","year_sold","sale_price"]
training_dataset = pd.read_csv('train.csv', names=column_name, header=0)
# Set Samples Array
X= training_dataset.iloc[:, 1:5].values
# Set Results 
Y = training_dataset.iloc[:, 5].values

# Set train and test data set for accuracy. 
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.2, random_state = 100)
# Define keys for results
total_results=numpy.concatenate([y_train, y_test])
uniques = numpy.unique(total_results)


# Set keys to y_train and y_test
for i in uniques:

	y_train[y_train == i] =numpy.where(uniques == i)[0]
	y_test[y_test == i] =numpy.where(uniques == i)[0]
	
# Import test.csv
column_name_test=["id","area","bedrooms","month_sold","year_sold"]
test_dataset = pd.read_csv('test.csv', names=column_name_test, header=0)
# Set Samples Array
test_x = test_dataset.iloc[:, 1:5].values



# Encoding Training Dataset
encoding_train_y = np_utils.to_categorical(y_train)

# Encoding Testing Dataset
encoding_test_y = np_utils.to_categorical(y_test)


# Create model
model = Sequential()
model.add(Dense(12, input_dim=4, init='uniform', activation='relu'))
model.add(Dense(4, init='uniform', activation='relu'))
model.add(Dense(len(uniques), init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['accuracy'])
# Fit the model
model.fit(X_train, encoding_train_y, epochs=1500, batch_size=10)

# Predict X_test 
predictions = model.predict_classes(X_test)
list_pred=predictions.tolist()
# Get Accuracy
win=0
for i in range(len(list_pred)):
	if(y_test[i]==list_pred[i]):
		win+=1

accuracy=win/len(list_pred) 
print("Accuracy: "+str(accuracy))

# Calculate Predictions
predictions = model.predict_classes(test_x)


# Convert Keys to Values
for i in predictions:
	if (i<len(uniques)):
		predictions[predictions == i]=uniques[i]

# Save results in .csv	
results=numpy.concatenate((test_x, numpy.array([predictions]).T), axis=1)
df = pd.DataFrame(results)
df.to_csv("neural-network-results.csv")
