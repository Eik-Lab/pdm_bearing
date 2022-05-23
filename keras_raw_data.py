from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import time
import pandas as pd
import numpy as np
from data_read import read_file, read_all_from_trial


input_dim = 500

# Read data from csv
def get_data(trial):
	
	# for health in ['H', 'I', 'O']:
	data_H = read_file(f'data/H-A-{trial}.mat')['Vibration']
	data_O = read_file(f'data/O-A-{trial}.mat')['Vibration']
	data_I = read_file(f'data/I-A-{trial}.mat')['Vibration']
		
	x = data_H.values.reshape(-1, input_dim)
	x = np.vstack((x, data_O.values.reshape(-1, input_dim)))
	x = np.vstack((x, data_I.values.reshape(-1, input_dim)))

	y = np.array([1, 0, 0]*int(len(x)/3)).reshape(-1, 3)
	y = np.vstack((y, np.array([0, 1, 0]*int(len(x)/3)).reshape(-1, 3)))
	y = np.vstack((y, np.array([0, 0, 1]*int(len(x)/3)).reshape(-1, 3)))

	return (x, y)

# split into input (X) and output (y) variables

x_train, y_train = get_data(1)
print(x_train.shape, y_train.shape)

x_val, y_val = get_data(2)




# define the keras model
model = Sequential()
model.add(Dense(500, input_dim=input_dim, activation='relu'))
model.add(Dense(250, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(150, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(48, activation='relu'))
model.add(Dense(48, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))


# compile the keras model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

start = time.time()

# # fit the keras model on the dataset
model.fit(x_train, y_train, epochs=40, batch_size=300, verbose=1, validation_data=(x_val, y_val))

end = time.time()
print(f'Training time: {end - start}')

# # evaluate the keras model
x_test, y_test = get_data(3)
_, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f'Accuracy: {accuracy*100:.2f}%')
