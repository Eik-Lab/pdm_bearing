from data_read import read_all_from_trial
from preprocessing import amplitude, frequency
import pandas as pd

data_dict = read_all_from_trial(2, 20)

new_data = {'amplitude': [], 'frequency': [], 'health': []}

for health in data_dict.keys():
    for data in data_dict[health]:

        freq = (frequency(data["Vibration"], window_size=1000) / frequency(data["Speed"], window_size=1000)).mean()
        amp = amplitude(data["Vibration"], n=100)

        new_data['amplitude'].append(amp)
        new_data['frequency'].append(freq)
        new_data['health'].append(health)

df = pd.DataFrame(new_data)
df.to_csv('amp_freq_data_2.csv', index=False)
