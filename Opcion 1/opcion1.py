
# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
from numpy import genfromtxt
from keras.utils import np_utils
import pandas as pd
from sklearn import preprocessing

# fix random seed for reproducibility

# load pima indians dataset
column_name=["id","area","bedrooms","month_sold","year_sold","sale_price"]
training_dataset = pd.read_csv('train.csv', names=column_name, header=0)

train_x = training_dataset.iloc[:, 1:5].values
print(train_x)
train_y = training_dataset.iloc[:, 5].values
uniques = numpy.unique(train_y)
print(uniques)

for i in uniques:
	print(i)
	train_y[train_y == i] =numpy.where(uniques == i)[0]
	

# Import testing dataset
column_name_test=["id","area","bedrooms","month_sold","year_sold"]
test_dataset = pd.read_csv('test.csv', names=column_name_test, header=0)
test_x = test_dataset.iloc[:, 1:5].values


print(train_y)
# Encoding training dataset
encoding_train_y = np_utils.to_categorical(train_y)
print(encoding_train_y[0])


# create model
model = Sequential()
model.add(Dense(12, input_dim=4, init='uniform', activation='relu'))
model.add(Dense(4, init='uniform', activation='relu'))
model.add(Dense(len(uniques), init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='hinge', optimizer='Adadelta', metrics=['accuracy'])
# Fit the model


model.fit(train_x, encoding_train_y, epochs=50, batch_size=10)

# calculate predictions
predictions = model.predict_classes(test_x)
print(predictions.tolist())
# round predictions
'''
rounded = [round(x[0]) for x in predictions]
print(rounded)
'''
