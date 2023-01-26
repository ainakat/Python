#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:36:01 2022

@author: aina
"""

##pip install pandas
#load packages
import pandas as pd
import numpy as np 
import csv as csv  
import os as os


## the first 20 lines of code are not being used anymore, but instead of deleting them, 
#I am commenting them out. 

#upload data
#grades = pd.read_csv("/Users/aina/Desktop/2022-11-08T1135_Grades-ECON_262.1002_Principles_of_Statistics_II.csv")

#identify columns (this will make it easier for me to clean the data)
#all_columns = grades.columns

#this hw score only includes hw1 - hw 4
#grades['hw_score'] = grades.iloc[:,5:9].sum(axis='columns')
#this score only includes quizzes 1-15
#grades['quiz_score'] = grades.iloc[:,11:26].sum(axis='columns')
#midterm 1 and midterm 2 scores
#grades['midterm1_score'] = grades['Midterm 1 Final Score']
#grades['midterm2_score'] = grades['Midterm 2 Final Score']

#drop unnecessary columns, we don't need these for analysis
#grades = grades.iloc[:,[0,2,113,114,115,116,35]]


#make list to store all survey dataframes
survey_data = []
dir_name = "/Users/aina/Documents/Teaching/ECON262_fall22/Data_Files/survey_data"

#loop through each file in directory and append to survey_data list
for file in os.listdir("/Users/aina/Documents/Teaching/ECON262_fall22/Data_Files/survey_data"):
    survey_data.append(pd.read_csv(os.path.join(dir_name,file)))

#drop unnecessary columns
for df in range(len(survey_data)):
    survey_data[df] = survey_data[df].iloc[:,[2,8,10]]
    survey_data[df] = survey_data[df].drop(survey_data[df].filter(regex='n correct').columns, axis=1)

#merge all survey data into 1 dataframe
all_surveys = survey_data[0].merge(survey_data[1], how="left", on="sis_id")

#merge all survey data into 1 dataframe
for df in range(2,14,1):
    all_surveys = all_surveys.merge(survey_data[df], how="left", on="sis_id")

#drop all na values
all_surveys = all_surveys.dropna()

#drop all apostrophes from columns, this will make it easier to rename columns
all_surveys.columns = all_surveys.columns.str.replace("'","")

#drop unnecessary columns
all_surveys = all_surveys.drop(['sis_id'], axis='columns')

#create dictionary that I'll use use to rename columns below
data_dict = {'Roll Call Attendance (1043013)':'attendance',
             '4199633: Approximately how many steps do you walk in a day? (If you are unsure, provide a rough estimation.) Enter a numerical value.':'daily_steps',
             '4091287: How many hours a week do you exercise (cardio, resistance training, aerobics, etc)? Enter an integer value.':'exercise_hours',
             '4199629: Approximately how many hours of sleep do you get each night? Enter a numerical value.':'sleep_hours',
             '4171904: From the following options, which is your favorite choice of fast food options?':'fav_fast_food',
             '4171906: Are you an iPhone or Android user?':'phone_type',
             '4225161: On a scale of 1 to 10, how much do you "like" school? (10 being very interested in school, 1 being absolutely not interested in school) Enter a numerical value.':'school_interest',
             '4091288: Which is your preferred fast-food option for fried chicken?\n\nIf you are vegan, and someone forced you to eat chicken, which would you choose?':'fav_chicken',
             '4091384: How many credits are you enrolled in this semester?':'enrolled_credits',
             '4091286: Approximately how much money do you spend on dining out on a weekly basis? (fast food, fine dining, anything that doesnt include the grocery store and home cooked meals)':'dining_spending',
             '4244017: From the options below, approximately how long is your commute to campus (on average)? (regardless of your method of transportation)':'commute_duration',
             '4243986: From the options below, how would you rate your current health status?':'health_status',
             '4243992: From the options below, which is your primary method of transportation to school?':'transportation',
             '4245152: How many hours a week do you spend studying or working on material for school on average? This includes homework, studying, working on assignments, group projects, etc. for all of your enrolled courses.':'study_hours',
             '4245155: On a scale of 1-10, how would you rate your current level of happiness in life? (10 being very happy, 1 being not that happy)':'happiness_score', 
             '4245159: On a scale of 1 to 10, how would you rate your success in higher education based on your experience as a college student? (10 being very successful, 1 being not that successful)':'success_score'}

#rename columns for convenience
all_surveys.rename(columns = data_dict, inplace = True)

#create list to store dummy columns for each categorical variable 
dummies = []

#create dummy columns for each categorical variable
dummies.append(pd.get_dummies(all_surveys.fav_fast_food))
dummies.append(pd.get_dummies(all_surveys.study_hours))
dummies.append(pd.get_dummies(all_surveys.phone_type))
dummies.append(pd.get_dummies(all_surveys.commute_duration))
dummies.append(pd.get_dummies(all_surveys.fav_chicken))
dummies.append(pd.get_dummies(all_surveys.enrolled_credits))
dummies.append(pd.get_dummies(all_surveys.health_status))
dummies.append(pd.get_dummies(all_surveys.dining_spending))
dummies.append(pd.get_dummies(all_surveys.transportation))

#merge dummies with whole dataframe
for df in range(len(dummies)):
    all_surveys = all_surveys.merge(dummies[df], left_index = True, right_index = True)

#create second dataframe that drops unnecessary variables
all_surveys2 = all_surveys.drop(['fav_fast_food','phone_type','commute_duration','study_hours',
                                 'fav_chicken','enrolled_credits','health_status','dining_spending',
                                 'transportation'], axis='columns')
#check columns
columns2 = pd.DataFrame(all_surveys2.columns)

#export to excel file
all_surveys2.to_excel("/Users/aina/Desktop/class_data.xlsx")







