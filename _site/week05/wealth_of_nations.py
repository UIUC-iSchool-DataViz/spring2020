import pandas as pd
import os
import numpy as np


def clean_data(data):
    for column in ['income', 'lifeExpectancy', 'population']:
        data = data.drop(data[data[column].apply(len) <= 4].index)
    return data

def extrap_interp(data):
    data = np.array(data)
    x_range = np.arange(1800, 2009, 1.)
    y_range = np.interp(x_range, data[:, 0], data[:, 1])
    return y_range

def extrap_data(data):
    for column in ['income', 'lifeExpectancy', 'population']:
        data[column] = data[column].apply(extrap_interp)
    return data

def process_data(filename):
    data = pd.read_json(os.path.abspath(filename))
    data = clean_data(data)
    data = extrap_data(data)
    return data

def get_min_max(data):
    income_min, income_max = np.min(data['income'].apply(np.min)), np.max(data['income'].apply(np.max))
    life_exp_min, life_exp_max = np.min(data['lifeExpectancy'].apply(np.min)), np.max(data['lifeExpectancy'].apply(np.max))
    pop_min, pop_max = np.min(data['population'].apply(np.min)), np.max(data['population'].apply(np.max))
    return income_min, income_max, life_exp_min, life_exp_max, pop_min, pop_max

def get_data(data,year, initial_year):
    year_index = year - initial_year
    income = data['income'].apply(lambda x: x[year_index])
    life_exp = data['lifeExpectancy'].apply(lambda x: x[year_index])
    pop =  data['population'].apply(lambda x: x[year_index])
    return income, life_exp, pop
    
    
