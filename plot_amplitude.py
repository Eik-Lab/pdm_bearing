import matplotlib.pyplot as plt
from data_read import read_file, split_data, read_all_from_trial
from preprocessing import amplitude, frequency

# create 2 subplots
fig, ax1 = plt.subplots(1, 1)
fig.suptitle("Amplitude", fontsize=16)
amplituder = {'H': [], 'O': [], 'I': []}
frekvenser = {'H': [], 'O': [], 'I': []}

data_list = read_all_from_trial(1, 20)

for health in data_list.keys():
    for data in data_list[health]:
        amplituder[health].append(amplitude(data["Vibration"], n=100))
        frekvenser[health].append((frequency(data["Vibration"], window_size=1000) / frequency(data["Speed"], window_size=1000)).mean())

alpha = 0.5
ax1.scatter(amplituder['H'], frekvenser['H'], label='Healthy', alpha=alpha)
ax1.scatter(amplituder['O'], frekvenser['O'], label='Outer defect', alpha=alpha)
ax1.scatter(amplituder['I'], frekvenser['I'], label='Inner defect', alpha=alpha)

ax1.legend()
ax1.set_xlabel('Amplitude')
ax1.set_ylabel('Frequency')
plt.show()
