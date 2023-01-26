#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:08:57 2022

@author: aina
"""

#further analysis to support why I chose to drop certain records 

#load packages
import pandas as pd
import numpy as np 
import math as math
import os as os
import csv as csv  



###########################
###########################PROOF THAT 2021 DFS ARE IDENTICAL, AND 2022 DFS
###########################


#proof that the two dataframes from 2021 are identical
df3 = pd.read_csv('/Users/aina/Documents/RAProjects/MLTSS/HHA data/2021/home_health_services_07_2021/HH_Provider_July2021.csv', encoding='cp1252')
df4 = pd.read_csv('/Users/aina/Documents/RAProjects/MLTSS/HHA data/2021/home_health_services_09_2021/HH_Provider_July2021.csv', encoding='cp1252')
df3.equals(df4)
    
#proof that the two dataframes from 2022 are not identical, but unsure?
df1 = pd.read_csv('/Users/aina/Documents/RAProjects/MLTSS/HHA data/2022/home_health_services_01_2022/HH_Provider_Jan2022.csv', encoding='cp1252')
df2 = pd.read_csv('/Users/aina/Documents/RAProjects/MLTSS/HHA data/2022/home_health_services_02_2022/HH_Provider_Jan2022.csv', encoding='cp1252')
df1.compare(df2)
df1.equals(df2)

###########################
###########################UNIQUE TIME STAMPS AND UNIQUE PNS OVER THE TIME PERIODS
###########################

def unique_times_pns():

    #number of unique time stamps over the years
    unique_time_stamps = pd.unique(dfmodified.t)
    
    #number of unique providers over the years and how many times they occur
    providerCounts = pd.DataFrame(pd.value_counts(fulldf.pn))
    
    #providers that I have for the entire time frame
    fullproviders = providerCounts[providerCounts['pn'] == 66]
    
    4042*66
    2014-1992
    11*18000
    11*23000
    #keep records that show up over entire time frame (66 time points), we lose 414446 records in this
    dfmodified = fulldf.groupby('pn').filter(lambda x : len(x)==66)
    
    state_zip_66 = pd.unique(df66.state)
    
    ###In df66, I have 4042 providers over 66 time periods, starting in 200312 and ending in 202201. It includes 4400 zip codes.
    ##In df2, I have 17064 providers. Each provider shows up at least 2x. It includes 7857 zip codes.
    ##In fulldf, I have 17138 providers. Some cover the entire 66 time periods, some do not. It includes 7875 zip codes.

    return fullproviders

####################
####################
####################CODE TO GET LIST OF VARIABLE NAMES FOR EACH YEAR
####################
####################


#create dfs for each year to compare variables across years 
def dfYear(topyear, bottomyear):
    newdf = fulldf.loc[(fulldf['t'] >= bottomyear) & (fulldf['t'] <= topyear)]
    newdf = newdf.dropna(axis=1, how='all')
    return newdf 

#store each year's df in this list
each_year = []

#define starting points for loop below
bottomyear_start = 200300
topyear_start = 200400
years = 20

#loop to create df for each year, store in each_year list 
for val in range(years):
    if bottomyear_start < 201920:
        newdf = dfYear(topyear_start, bottomyear_start)
        each_year.append(newdf)
        topyear_start += 100
        bottomyear_start += 100
        newdf = []

#clean up variable explorer
del bottomyear_start, topyear_start, newdf, val, years

#list to store variable names 
variableNames = []
start_year = 2003

#loop through each df in each_year and store variable names 
for val in range(len(each_year)):
    variable_names = pd.DataFrame(each_year[val].columns, columns=['variables'])
    variable_names['vars'] = start_year
    variableNames.append(variable_names)
    variable_names = []
    start_year += 1
  
#clean up variable explorer
del val, variable_names

#create df of all variable names
allcolumns = pd.DataFrame(fulldf.columns, columns=['variables'])

#merge each year's df with allcolumns df 
for dfs in range(17):
    allcolumns = variableNames[dfs].merge(allcolumns, how = 'right', on = ['variables'])


data_dict_df = pd.DataFrame(data_dict.items(), columns=['meaning','abbreviation'])

allcolumns = data_dict_df.merge(allcolumns, how = 'right', right_on=('variables'), left_on=('abbreviation'))



#send df with all variables and each year's variables to excel 
allcolumns.to_excel("/Users/aina/Desktop/variables_by_year2.xlsx", sheet_name='variables')




###########################
###########################PROGRAM TO SEE WHICH PNS SHOW UP IN WHICH TIME PERIODS
###########################

def unique_pns():

    #unique provider numbers in the entire dataset
    pns = pd.DataFrame(pd.unique(dfmodified.pn), columns=['pn'])
    
    #select only pn and t columns from dfmodified
    pns_year = dfmodified[['pn','t']]
    
    #list to store individual pns for each year
    ind_pns= []
    
    #loop to create df for each unique provider number and the years they appear
    for val in pns.pn:
        df = pns_year[pns_year.pn == val]
        ind_pns.append(df)
    
    #create lists for each year to store marks if pn shows up in these years
    yr_append = [[] for _ in range(0,66)]
    
    #list of each of the 66 unique time periods
    yrs2 = [200312, 200403, 200406, 200409, 200412,200503, 200506, 200509, 200512,200603, 200606, 200609, 200612,
           200703, 200706, 200709, 200712,200803, 200806, 200812,200903, 200906, 200912,
           201001, 201004, 201010,201101, 201104, 201107, 201110,201201, 201204, 201207, 201210,
           201301, 201304, 201307, 201310,201401, 201404, 201407, 201410,201501, 201504, 201507, 201510,
             201601, 201604, 201607, 201610,201701, 201704, 201707, 201710,201801, 201804, 201807,201901, 201903, 201906, 201910,
             202001, 202010,202107,202201, 202202]
    
    
    #define function to mark a "1" or "0" if a pn shows up in a specific time period 
    def year_append1(yr,listappend):
        
        for df in range(len(ind_pns)):
            if yrs2[yr] in ind_pns[df].t.values:
                listappend.append('1')
            else:
                listappend.append('0')
                
        return listappend
    
    #loop through function for each of the 66 time periods 
    for val in range(len(yr_append)):
        yr_append[val] = year_append1(val, yr_append[val])
    
    #merge all lists with pns df 
    for val in range(len(yr_append)):
        pns[val] = yr_append[val]
    
    
    #create dictionary to rename columns according to time period
    dict2 = {0:'200312', 1: '200403', 2:'200406', 3:'200409', 4:'200412',5:'200503', 6:'200506', 7:'200509', 8:'200512',9:'200603', 10:'200606', 11:'200609', 12:'200612',
           13:'200703', 14:'200706', 15:'200709', 16:'200712',17:'200803', 18:'200806', 19:'200812',20:'200903', 21:'200906', 22:'200912',
           23:'201001', 24:'201004', 25:'201010',26:'201101', 27:'201104', 28:'201107', 29:'201110',30:'201201', 31:'201204', 32:'201207', 33:'201210',
           34:'201301', 35:'201304', 36:'201307', 37:'201310',38:'201401', 39:'201404', 40:'01407', 41:'201410',42:'201501', 43:'201504', 44:'201507', 45:'201510',
             46:'201601', 47:'201604', 48:'201607', 49:'201610',50:'201701', 51:'201704', 52:'201707', 53:'201710',54:'201801', 55:'201804', 56:'201807',57:'201901', 58:'201903', 59:'201906', 60:'201910',
             61:'202001', 62:'202010',63:'202107',64:'202201', 65:'202202'}
    
    #rename columns using dict2
    pns.rename(columns = dict2, inplace = True)
    
    #export finished dataframe to excel 
    pns.to_excel("/Users/aina/Desktop/pn_years.xlsx", sheet_name='years')

    return pns


###########################
###########################ZIP CODE/COUNTY PROBLEMATIC MERGING AND MATCHING 
###########################

def unique_zips():

    #array of unique zip codes 
    unique_zips = pd.unique(fulldf.zip)
    
    #import excel of county and matching zip codes 
    zip_county = pd.read_excel("/Users/aina/Documents/RAProjects/hospital closures/ZIP_COUNTY_092021.xlsx")
    
    #drop unnecessary columns 
    zip_county = zip_county.drop(['USPS_ZIP_PREF_CITY','USPS_ZIP_PREF_STATE','RES_RATIO','BUS_RATIO','OTH_RATIO','TOT_RATIO'], axis = 1)
    
    #create df of just zip codes 
    fulldf_zips = pd.DataFrame(fulldf.zip)
    
    #rename columns in order to match in the future 
    zip_county.rename(columns={'ZIP':'zip'}, inplace=True)
    
    #merge zip codes and county codes 
    merged_df = fulldf_zips.merge(zip_county, how = 'inner', on = ['zip'])
    
    #drop all duplicate records
    unique = merged_df.drop_duplicates()
    
    #One county can have multiple codes, so when I merge, it duplicates the records.
    merged_df2 = fulldf.merge(zip_county, how = 'inner', on = ['zip'])
    
    merged_df2 = merged_df2.drop_duplicates()
    
    return merged_df2


