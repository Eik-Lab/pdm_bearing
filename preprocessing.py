import pandas as pd

def frequency(data, window_size=10):
    """
    Calculate the frequency of a series.
    """ 
    data_mean = data.mean()

    bool_data = data > data_mean
    shifted_data = bool_data.shift(-1)

    state_change_data = bool_data != shifted_data
    frequency = state_change_data.rolling(window=window_size).sum()
    
    return frequency

def frequency_IQR(data, window_size=10):
    """
    Calculate the frequency of a series.
    """ 
    data_mean = data.mean()
    data_max = data[data > data_mean].mean()
    data_min = data[data < data_mean].mean()

    above = data > data_max
    below = (data < data_min) * -1
    combine = above + below

    bool_data = combine[combine != 0]
    shifted_data = bool_data.shift(-1)

    state_change_data = bool_data != shifted_data
    frequency = state_change_data.rolling(window=window_size).sum()
    
    return frequency

def amplitude(data, n=10):
    top_n = data.nlargest(n).mean()
    bottom_n = data.nsmallest(n).mean()

    return (top_n - bottom_n)/2

