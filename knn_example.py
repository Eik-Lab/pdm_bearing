from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd


# Load data
data = pd.read_csv('data_ml/amp_freq_data_1.csv')

# Create model
classifier = SVC(kernel='poly')
# classifier = KNeighborsClassifier()

# Train model
classifier.fit(data[['amplitude', 'frequency']], data['health'])

# Evaluate model
X_test = pd.read_csv('data_ml/amp_freq_data_2.csv')
score = classifier.score(X_test[['amplitude', 'frequency']], X_test['health'])
print(f'Score = {score*100:.2f}%')



