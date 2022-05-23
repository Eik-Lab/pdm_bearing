import matplotlib.pyplot as plt
from data_read import read_file
from preprocessing import frequency, frequency_IQR

# speed_condition = 'A'
data_list = [f'H-A-1']#, 'H-B-1', 'H-C-1', 'H-D-1']

# create 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("Vibration and speed over time", fontsize=16)

for data_name in data_list:
    data = read_file(f'data/{data_name}.mat').iloc[:10000]
    data['Speed'] = frequency(data['Speed'], 1000)
    # data['Vibration'] = frequency_IQR(data['Vibration'].rolling(10).mean(), 100000) / data['Speed']

    ax1.plot(data['Vibration'])
    # ax1.hlines(data['Vibration'].mean(), 0, len(data['Vibration']), linestyles='dashed')
    ax1.set_ylabel('Vibration')

    ax2.plot(data['Speed'])
    # ax2.hlines(data['Speed'].mean(), 0, len(data['Speed']), linestyles='dashed')
    ax2.set_ylabel('Speed')

ax1.legend(data_list)
ax2.legend(data_list)
plt.show()
