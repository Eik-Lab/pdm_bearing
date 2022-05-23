import re
import matplotlib.pyplot as plt
from preprocessing import amplitude, frequency
from data_read import read_file


healths = ['H', 'I', 'O']
speeds = ['A', 'B', 'C', 'D']
trails = ['1']

for health in healths:
    for speed in speeds:
        for trail in trails:
            data = read_file(f'../data/{health}-{speed}-{trail}.mat')
            data.to_csv(f'../csv/{health}-{speed}-{trail}.csv', index=False)
            print(f'{health}-{speed}-{trail} done!')

