import requests
import time
from random import gauss
import numpy as np
from numpy import arange
from matplotlib.pyplot import bar
from scipy.stats import norm, expon
from statistics import median
import matplotlib.pyplot as plt
import datetime
import math


def API_data(market, start_date, end_date):
    timestamp_start = int(start_date.replace(tzinfo=datetime.timezone.utc).timestamp())
    timestamp_end = int(end_date.replace(tzinfo=datetime.timezone.utc).timestamp())
    url = f"https://www.bitstamp.net/api/v2/ohlc/{market}usd?step=86400&end={timestamp_end}&start={timestamp_start}&limit={(end_date - start_date).days}"
   
    answer = requests.get(url).json()['data']['ohlc']

    volume=[]
    change=[]
    for i in range(len(answer) - 1):
        volume.append(float(answer[i]['volume']))
    for i in range(1,len(volume)):
        change.append(abs((volume[i] - volume[i - 1]) / volume[i]))    
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

def plot_data(actual_data,single_simulation, many_simulations):
   
    plt.figure(figsize=(20, 10))
    plt.subplot(2, 2, 1)
    plt.plot(actual_data, '-r')
    plt.title("Actual data")
    plt.subplot(2, 2, 2)
    plt.plot(single_simulation, '-g')
    plt.title("Single simulation")
    plt.subplot(2, 2, 3)
    plt.plot(many_simulations, '-b')
    plt.title("Average from 100 simulations")
    plt.suptitle('Dane rzeczywiste vs dane przewidywane', fontsize=18)
    plt.show()
    
   
def run(market, training_start_date, training_end_date, simulation_start_date, simulation_end_date):
    
    historical_change, historical_volume = API_data(market, training_start_date, training_end_date)
    _, actual_volume = API_data(market, simulation_start_date, simulation_end_date)
   
    prediction_period = len(actual_volume)
    
    predictions = make_prediction(historical_change, historical_volume,prediction_period)
    with open('dane_faktyczne.txt', 'w') as f:
        for data in historical_volume:
            f.write(str(data))
            f.write('\n')
    with open('pojedyncza_symulacja.txt', 'w') as f:
        for data in predictions:
            f.write(str(data))
            f.write('\n')
    averaged_predictions = []
    avg_predictions = []
    for _ in range(100):
        averaged_predictions.append(make_prediction(historical_change, historical_volume, prediction_period))
    with open('usrednione_100_symulacji.txt', 'w') as f:
        for i in range(len(averaged_predictions[0])):
            sum = 0
            for j in range(len(averaged_predictions)):
                sum += averaged_predictions[j][i]
            avg_predictions.append(float(sum)/len(averaged_predictions))    
            f.write(str(float(sum) / len(averaged_predictions)) )
            f.write('\n')   
    return actual_volume, predictions, avg_predictions 

training_start_date = datetime.datetime.strptime('01-05-2019', '%d-%m-%Y')
training_end_date = datetime.datetime.strptime('30-09-2019', '%d-%m-%Y')
simulation_start_date = datetime.datetime.strptime('01-10-2019', '%d-%m-%Y')
simulation_end_date = datetime.datetime.strptime('01-05-2020', '%d-%m-%Y')
real_data, single_run, avg_run = run('btc', training_start_date, training_end_date, simulation_start_date, simulation_end_date)
e1 = []
e2 = []
for i in range(len(single_run)):
    e1.append ((real_data[i] - single_run[i])*(real_data[i] - single_run[i] ))
    e2.append((real_data[i] - avg_run[i] )*(real_data[i] - avg_run[i] )) 

root_mean_square_error_single_run = math.sqrt(sum(e1)/len(e1))
root_mean_square_error_avg_run = math.sqrt(sum(e2)/len(e2))   

print ('root mean square error for single run: ', root_mean_square_error_single_run)
print ('root mean square error for averaged run (100 simulations): ', root_mean_square_error_avg_run )
plot_data(real_data, single_run, avg_run)