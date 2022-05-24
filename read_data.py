import pandas as pd
import scipy.io
'''
First symbol:
H - healthy
I - faulty with an inner race defect
O - faulty with an outer race defect.

Second symbol:
A - increasing speed
B - decreasing speed
C - increasing then decreasing speed
D - decreasing then increasing speed

Third symbol:
1 - trial one
2 - trial two
3 - trial three
'''

def read_mat_file(file_name):
    mat = scipy.io.loadmat(file_name)
    channel_1 = mat['Channel_1'].flatten()
    channel_2 = mat['Channel_2'].flatten()
    return pd.DataFrame({'Vibration': channel_1, 'Speed': channel_2}, index=range(len(channel_1)))

def read_all_from_trial(trial_number, split_count):
    speed_condition = ['A', 'B', 'C', 'D']
    health_condition = ['H', 'O', 'I']

    data_list = {'H': [], 'O': [], 'I': []}

    for health in health_condition:
        for speed in speed_condition:
            data_name = f'{health}-{speed}-{trial_number}.mat'
            data_list[health] += split_data(read_mat_file('data_raw/' + data_name), split_count)

    return data_list

def split_data(data, number_of_chunks=2):
    chunks = []
    chunck_size = len(data) / number_of_chunks
    
    for i in range(number_of_chunks):
        chunks.append(data[int(i*chunck_size):int((i+1)*chunck_size)])

    return chunks
