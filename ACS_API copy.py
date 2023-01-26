#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:15:18 2022

@author: aina
"""

#allows us to make API calls
import requests
#allows us to manipulate data as a dataframe
import pandas as pd


#assign year variable
years = ['2013','2014','2015','2016','2017','2018','2019']

#assign variables
vars_i_want = 'DP05_0066PE,DP05_0060PE,DP03_0112PE,DP05_0001E'

#create empty list to store ACS datas
datas = []

counter = 2013

#loop through each year, pulling data from API, cleaning & storing in datas list
for year in years:
    
    ##acs 5 yr subject table url
    url = 'https://api.census.gov/data/'+year+'/acs/acs5/profile?get='+vars_i_want+'&for=county:*&in=state:*&key=341ab837786b66b32e6e00e9645c82c0b8678053'
    
    #make API request
    api_req = requests.get(url).json()
    
    #notes
    #DP05_0066PE=Percent!!Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)
    #DP05_0060PE=Percent!!Estimate!!Race alone or in combination with one or more other races!!Total population!!Black or African American
    #DP03_0103E=Number!!Estimate!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All families
    #DP05_0001E=Number!!Estimate!!SEX AND AGE!!Total population
    
    
    #create df to store all commodity codes
    alldata = pd.DataFrame(columns=["hispanic_percent","black_percent","poverty_percent","total_pop","state_fips","county_fips"])
            
    
    #for each commodity code in commodities, append it to the dataframe, "commodities" 
    for record in range(1,len(api_req),1):
        hispanic_percent2 = api_req[record][0]
        black_percent2 = api_req[record][1]
        poverty_percent2 = api_req[record][2]
        total_pop2 = api_req[record][3]
        state2 = api_req[record][4]
        county2 = api_req[record][5]
        alldata = alldata.append({'hispanic_percent':hispanic_percent2,'black_percent':black_percent2,'poverty_percent':poverty_percent2,'total_pop':total_pop2,'state_fips':state2,'county_fips':county2}, ignore_index=True)
    
    
    #coerce fips column to floats
    alldata['state_fips'] = alldata['state_fips'].astype(float)
    alldata['county_fips'] = alldata['county_fips'].astype(float)
    
    #load fips codes excel file
    fips = pd.read_excel("/Users/aina/Documents/RAProjects/MLTSS/acs_api/statefips.xlsx")
    
    #separate into state & county fips codes
    fips = pd.concat([fips['AL,01,001,Autauga County,H1'], fips['AL,01,001,Autauga County,H1'].str.split(',', expand=True)], axis=1)
    
    #drop unnecessary columns
    fips = fips.iloc[:,[1,2,3,4]]
    
    #rename columns for merging purposes later
    fips = fips.rename(columns={fips.columns[0]: 'state'})
    fips = fips.rename(columns={fips.columns[1]: 'state_fips'})
    fips = fips.rename(columns={fips.columns[2]: 'county_fips'})
    fips = fips.rename(columns={fips.columns[3]: 'county'})
    
    #coerce strings to floats for merging purposes later
    fips['county_fips'] = fips['county_fips'].astype(int)
    fips['state_fips'] = fips['state_fips'].astype(int)
    
    #drop "county" string
    fips.county = fips.county.str.replace("County","")
    
    #merge with all data
    alldata = alldata.merge(fips, how="left", on=['state_fips','county_fips'])
    
    #delete all empty spaces, for merging purposes later
    alldata['county'] = alldata['county'].str.replace(" ","")
    
    #convert poverty and total population columns to floats
    alldata['poverty_percent'] = alldata['poverty_percent'].astype(float)
    alldata['total_pop'] = alldata['total_pop'].astype(float)
    
    alldata['t2'] = counter
    
    counter =+ counter+ 1
    
    datas.append(alldata)
    
#concatenate data into one final df
final_df = pd.concat(datas, ignore_index=True)

final_df['t2'] = final_df['t2'].astype(str)


#export final df to excel
final_df.to_excel("/Users/aina/Documents/RAProjects/MLTSS/acs_api/acs_clean.xlsx")



