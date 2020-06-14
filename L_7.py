import requests
import time
from random import gauss
import numpy as np
from numpy import arange
from matplotlib.pyplot import bar
from scipy.stats import norm, expon
from statistics import median
import matplotlib.pyplot as plt

def API_data(market, days):
    timestamp = str(int(time.time()) - 86400 * days)
    url = f"https://www.bitstamp.net/api/v2/ohlc/{market}usd?step=86400&limit=100&start={timestamp}"
    answer = requests.get(url).json()['data']['ohlc']
    volume=[]
    change=[]
    for i in range(len(answer)):
        volume.append(float(answer[i]['volume']))
    for i in range(1,len(volume)):
        change.append( ((volume[i] - volume[i - 1]) / volume[i]))    
    return change, volume

def make_prediction(data, volumen,days):
    change_avg, change_std = expon.fit(data)
    vol_avg, vol_std = expon.fit(volumen) 
    future = []
    for i in range(days):
        predict_change =  abs(gauss(change_avg,  change_std))
        predicted_value =  predict_change * abs(gauss(vol_avg, vol_std)) 
        future.append( predicted_value)
    return future   


def plot_data(historical_data,future_data):
    plt.grid(True)
    bar(arange(0, len(historical_data)), historical_data, color='red')
    bar(arange(len(historical_data), len(future_data) + len(historical_data)), future_data, color='blue')
    plt.ylabel("Volumen")
    plt.legend(('Historical data','Prediction'))
    plt.show()
   
def run(market, days):
    change, volumen = API_data(market, days)
    future=make_prediction(change, volumen,days)
    plot_data(volumen,future)
run('btc', 30)