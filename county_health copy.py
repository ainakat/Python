#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 08:31:08 2022

@author: aina
"""
#load packages
import pandas as pd 
import numpy as np 
import csv as csv  
import os as os
import glob

#define folder path on computer
folder = '/Users/aina/Documents/RAProjects/MLTSS/county_health_rank/analytic data'
#get csv files list from folder
csv_files = glob.glob(folder + "/*.csv")

#load csv files into data_files list
data_files = (pd.read_csv(file, skiprows=1) for file in csv_files)

#concatenate all dfs into one big df 
big_df = pd.concat(data_files, ignore_index=True)

#only include columns that contain 'rawvalue/state/county/fips' strings or focus variables
big_df = big_df.loc[:, big_df.columns.str.contains('state|county|fips|year|v001_rawvalue|v002_rawvalue|v036_rawvalue|v070_rawvalue|v085_rawvalue|v007_rawvalue|v060_rawvalue')]
#drop rows that contain United states values
big_df = big_df[big_df['county'] != 'United States']

#convert fipscode column to string for merging purposes later
big_df['FIPS'] = big_df['fipscode'].astype(str)
big_df['FIPS'] = big_df['FIPS'].str.replace('.0','')

#create t2 column as string type of year column
big_df['t2'] = big_df['year'].astype(str)
#drop last two digits in t2 column
big_df['t2'] = big_df['t2'].str[:-2]



#export final df to excel
big_df.to_excel("/Users/aina/Documents/RAProjects/MLTSS/county_health_rank/county_health_clean.xlsx")




