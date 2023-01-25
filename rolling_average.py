import pandas as pd
import numpy as np

def rolling_avg(df, duration, error, column):
    '''The rolling().mean() method finds the rolling average for the specified number of instances. 
        The anomaly detection checks if each value is higher than the 3 week rolling average.'''
    
    df["rolling_average"] = df[column].rolling(duration).mean()
    df["var"] = df["rolling_average"] * error
    df["lower_bound"] = df["rolling_average"] - df["var"]
    df["upper_bound"] = df["rolling_average"] + df["var"]
    df["anomaly"] = np.where(df[column] > df['upper_bound'], 1, 0)
    
    return df