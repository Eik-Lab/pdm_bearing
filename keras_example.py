from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd


# Import data and split into training and test sets
def get_data(file_name):
	
	data = pd.read_csv(file_name)

	x = data[['amplitude', 'frequency']]

	y = pd.DataFrame()
	y['H'] = data['health'] == 'H'
	y['I'] = data['health'] == 'I'
	y['O'] = data['health'] == 'O'

	return (x, y)

# Load data
x_train, y_train = get_data('data_ml/amp_freq_data_1.csv')
x_val, y_val = get_data('data_ml/amp_freq_data_2.csv')

# Create model
model = Sequential()
model.add(Dense(12, input_dim=2, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=100, batch_size=10, verbose=1, validation_data=(x_val, y_val))

# Evaluate model
x_test, y_test = get_data('data_ml/amp_freq_data_3.csv')
_, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f'Accuracy: {accuracy*100:.2f}%')
