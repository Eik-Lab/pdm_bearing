from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from data_read import read_all_from_trial
import pandas as pd
import matplotlib.pyplot as plt
import time

data = pd.read_csv('amp_freq_data_1.csv')

classifier = SVC(kernel='poly')
# classifier = KNeighborsClassifier()

start = time.time()

classifier.fit(data[['amplitude', 'frequency']], data['health'])

end = time.time()
print(f'Training time: {end - start}')

# Test data on set 2

X_test = pd.read_csv('amp_freq_data_2.csv')

score = classifier.score(X_test[['amplitude', 'frequency']], X_test['health'])

print(f'Score = {score*100:.2f}%')



