#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:35:50 2022

@author: aina
"""

##pip install pandas
#load packages
import pandas as pd
import numpy as np 
#import math as math
import os as os
import csv as csv  

#all data cleanup procedures wrapped up in 2 functions
def datacleanup():

    
    #function to load & concatenate all files 
    def load_concat2(file_name, folder_path, counter, year_list, code):
        
        #load all 2004 csv files and append to year_list
        for folder in folder_path:
            year_list.append(pd.read_csv(os.path.join(folder, file_name),
                                       encoding=code))
        
        #add column identifying time of data 
        for df in year_list:
            df['t'] = counter
            counter += 3
                    
        return year_list
        
    
    #path to all folders with csv files
    
    f_03 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2003/HHCArchive_20031201']   
    f_04 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2004/HHCArchive_20040301',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2004/HHCArchive_20040601',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2004/HHCArchive_20040901',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2004/HHCArchive_20041201']
    f_05 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2005/HHCArchive_20050301',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2005/HHCArchive_20050601',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2005/HHCArchive_20050901',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2005/HHCArchive_20051201']
    f_06 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2006/HHCArchive_20060301',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2006/HHCArchive_20060601',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2006/HHCArchive_20060901',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2006/HHCArchive_20061201']
    f_07 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2007/HHCArchive_20070301',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2007/HHCArchive_20070601',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2007/HHCArchive_20070901',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2007/HHCArchive_20071201']
    f_08 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2008/HHCArchive_20080301',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2008/HHCArchive_20080601',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2008/HHCArchive_20081201']
    f_09 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2009/HHCArchive_20090301',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2009/HHCArchive_20090601',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2009/HHCArchive_20091201']
    f_10 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2010/HHCArchive_20100101',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2010/HHCArchive_20100401',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2010/HHCArchive_20101001']
    f_11 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2011/HHCArchive_20110101',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2011/HHCArchive_20110401',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2011/HHCArchive_20110701',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2011/HHCArchive_20111001']
    f_12 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2012/HHCArchive_20120101',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2012/HHCArchive_20120401',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2012/HHCArchive_20120701',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2012/HHCArchive_20121001']
    f_13 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2013/HHCArchive_20130101',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2013/HHCArchive_20130401',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2013/HHCArchive_20130701',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2013/HHCArchive_20131001']
    f_14 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2014/HHCArchive_Revised_FlatFiles_20140101',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2014/HHCArchive_Revised_FlatFiles_20140417',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2014/HHCArchive_Revised_FlatFiles_20140717',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2014/HHCArchive_Revised_FlatFiles_20141023']
    f_15 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2015/hhs_revised_flatfiles_archive_01_2015',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2015/HHCArchive_Revised_FlatFiles_20150416',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2015/hhs_revised_flatfiles_archive_07_2015',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2015/hhs_revised_flatfiles_archive_10_2015']
    f_16 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2016/hhs_revised_flatfiles_archive_01_2016',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2016/hhs_revised_flatfiles_archive_04_2016',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2016/hhs_revised_flatfiles_archive_07_2016',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2016/hhs_revised_flatfiles_archive_10_2016']
    f_17 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2017/HHCompare_Revised_FlatFiles',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2017/hhs_revised_flatfiles_archive_04_2017',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2017/hhs_revised_flatfiles_archive_07_2017',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2017/hhs_revised_flatfiles_archive_10_2017']
    f_18 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2018/hhs_revised_flatfiles_archive_01_2018',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2018/hhs_revised_flatfiles_archive_04_2018',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2018/hhs_revised_flatfiles_archive_07_2018']
    f_19 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2019/hhs_revised_flatfiles_archive_01_2019',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2019/hhs_revised_flatfiles_archive_03_2019',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2019/hhs_revised_flatfile_archive_06_2019',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2019/hhs_revised_flatfile_archive_10_2019']
    f_20 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2020/hhs_revised_flatfiles_archive_01_2020',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2020/home_health_services_archive_8_2020',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2020/home_health_services_archive_10_2020']
    f_21 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2021/home_health_services_07_2021',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2021/home_health_services_09_2021']
    f_22 = ['/Users/aina/Documents/RAProjects/MLTSS/HHA data/2022/home_health_services_01_2022',
                '/Users/aina/Documents/RAProjects/MLTSS/HHA data/2022/home_health_services_02_2022']
    
    
    f_list = [f_03, f_04, f_05, f_06, f_07, f_08, f_09, f_10, f_11, f_12, f_13, f_14, f_15, f_16, f_17, f_18, f_19, f_20, f_21, f_22]
    del f_03, f_04, f_05, f_06, f_07, f_08, f_09, f_10, f_11, f_12, f_13, f_14, f_15, f_16, f_17, f_18, f_19, f_20, f_21, f_22
    
    year_list = []
    df_list = []
    
    count_start04 = 200403
    count_start10 = 201001
    
    for list in range(len(f_list)):
        if "2003" in f_list[list][0]: 
            df_list.append(load_concat2('Provider_2003_12.csv', f_list[list], 200312, year_list, 'ascii'))
            year_list = []
        elif "2004" in f_list[list][0] or "2005" in f_list[list][0] or "2006" in f_list[list][0] or "2007" in f_list[list][0]:
            df_list.append(load_concat2('Provider.csv', f_list[list], count_start04, year_list, 'ascii'))
            year_list = []
            count_start04 += 100
        elif "2008" in f_list[list][0] or "2009" in f_list[list][0]:
            df_list.append(load_concat2('Provider.csv', f_list[list], count_start04, year_list, 'ascii'))
            year_list = []
            count_start04 += 100
        elif "2010" in f_list[list][0] or "2011" in f_list[list][0] or "2012" in f_list[list][0] or "2013" in f_list[list][0]:
            df_list.append(load_concat2('Provider.csv', f_list[list], count_start10, year_list, 'cp1252'))
            year_list = []
            count_start10 += 100
        elif "2014" in f_list[list][0] or "2015" in f_list[list][0] or "2016" in f_list[list][0] or "2017" in f_list[list][0] or "2018" in f_list[list][0] or "2019" in f_list[list][0] or "2020" in f_list[list][0]:
            df_list.append(load_concat2('HHC_SOCRATA_PRVDR.csv', f_list[list], count_start10, year_list, 'cp1252'))
            year_list = []
            count_start10 += 100
        elif "2021" in f_list[list][0]:
            df_list.append(load_concat2('HH_Provider_July2021.csv', f_list[list], count_start10, year_list, 'cp1252'))
            year_list = []
            count_start10 += 100
        elif "2022" in f_list[list][0]:
            df_list.append(load_concat2('HH_Provider_Jan2022.csv', f_list[list], count_start10, year_list, 'cp1252'))
            year_list = []
            count_start10 += 100
    
    del list, count_start04, count_start10, year_list
    
    #separate dataframe lists into 4 lists based on how many quarters are in each dataframe list
    list01 = [df_list[0]]
    list04 = [df_list[1],df_list[2],df_list[3],df_list[4],df_list[8],df_list[9],df_list[10],df_list[11],df_list[12],df_list[13],df_list[14],df_list[16]]
    list03 = [df_list[5],df_list[6],df_list[7],df_list[15],df_list[17]]
    list02 = [df_list[18],df_list[19]]
    
    #define function to remove strange icons from column names & remove "footnote" columns
    def removeicons(each_list): 
        for year in range(len(each_list)):
            for quarter in range(len(each_list[0])):
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("'","")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace(",","")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("`","")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("patientsâ€™","")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("doctorâ€™s","doctors")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("patients’","patients")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("pain ","pain")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("pain  ","pain")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("?","")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace(".","")
                each_list[year][quarter].columns = each_list[year][quarter].columns.str.replace("doctor’s","doctors")
                each_list[year][quarter] = each_list[year][quarter].drop(each_list[year][quarter].filter(regex='Footnote').columns, axis=1)
        return each_list
    
    #apply removeicons to all years except 2003
    for item in [list01, list02, list03, list04]:
        item = removeicons(item)
    
    #clean up unnecessary variables
    del item 
        
    #store unqiue column names in colnames list to rename in next step
    colnameslist = []
    
    #define function to pull column names from each df 
    def colnames(each_list, nameslist):
        for year in range(len(each_list)):
            for quarter in range(len(each_list[0])):
                a = each_list[year][quarter].columns
                nameslist.append(a)
        
        return nameslist
    
    #define function to flatten list of lists into 1 array and only pull unique column names 
    def uniquecolnames(nameslist):
        allnames = [x for l in nameslist for x in l]
        allnames = pd.unique(allnames)
        return allnames
        
    #apply functions to all lists
    for item in [list01, list02, list03, list04]:
        colnames(item, colnameslist)          
    
    colnameslist = uniquecolnames(colnameslist)
    
    #data dictionary to use to rename columns
    data_dict = {'ProviderNum':'pn','ProviderName':'name','StreetAddress':'address','City':'city', 'State':'state','ZipCode':'zip','Telephone':'phone',
    'OwnershipType':'owner_type','DateCertified':'date_cert','Nursing Care Services':'nc_serv','Physical Therapy Services':'pt_serv','Occupational Therapy Services':'ot_serv','Speech Pathology Services':'sp_serv','Medical Social Services':'ms_serv','Home Health Aide Services':'hha_serv',
    'Percentage of patients who get better at walking or moving around':'gb_walking','Percentage of patients who get better at getting in and out of bed':'gb_bed',
    'Percentage of patients who get better at getting to and from the toilet':'gb_toilet','Percentage of patients who have less painwhen moving around':'less_pain',
    'Percentage of patients who get better at bathing':'gb_bathing','Percentage of patients who get better at taking their medicines correctly (by mouth)':'gb_medicine',
    'Percentage of patients who get better at getting dressed':'gb_dressed','Percentage of patients who stay the same (dont get worse) at bathing':'same_bathing',
    'Percentage of patients who had to be admitted to the hospital':'hosp_admit','Percentage of patients who need urgent unplanned medical care':'need_urgent_care',
    'Percentage of patients who are confused less often':'confused_less','Skilled Nursing Care':'nc_serv', 
    'Physical Therapy':'pt_serv','Occupational Therapy':'ot_serv','Speech Pathology':'sp_serv','Medical Social':'ms_serv',
    'Home Health Aide':'hha_serv','Percentage of patients whose bladder control improves':'bc_improves','Percentage of patients who are short of breath less often':'sbreath_lessoften',
    'Percentage of patients who stay at home after an episode of home health care ends':'stayhome_afterhhc','Percentage of patients who need unplanned medical care related to a wound that is new is worse or has become infected':'unplanned_mc',
    'Percentage of patients whose wounds improved or healed after an operation':'wounds_improved','Nursing':'nc_serv',
    'Physical':'pt_serv','Speech Therapy':'sp_serv','How often the home health team began their patients care in a timely manner ':'hh_timely',
    'How often the home health team taught patients (or their family caregivers) about their drugs':'hh_tpatients_drugs',
    'How often the home health team checked patients risk of falling':'hh_check_fallrisk','How often the home health team checked patients for depression':'hh_check_dep',
    'How often the home health team determined whether patients received a flu shot for the current flu season':'hh_fluvax',
    'How often the home health team determined whether their patients received a pneumococcal vaccine (pneumonia shot)':'hh_pneumoniavax',
    'For patients with diabetes how often the home health team got doctors orders gave foot care and taught patients about foot care ':'hh_diabetes_footcare',
    'How often the home health team checked patients for pain ':'hh_paincheck','How often the home health team treated their patients pain ':'hh_paintreat',
    'How often the home health team treated heart failure (weakening of the heart) patients symptoms ':'hh_treatheart',
    'How often the home health team took doctor-ordered action to prevent pressure sores (bed sores) ':'hh_doctor_action_sores',
    'How often the home health team included treatments to prevent pressure sores (bed sores) in the plan of care ':'hh_treatsores',
    'How often the home health team checked patients for the risk of developing pressure sores (bed sores) ':'hh_check_sores',
    'How often patients got better at walking or moving around':'gb_walking2','How often patients got better at getting in and out of bed ':'gb_bed2',
    'How often patients got better at bathing':'gb_bathing2','How often patients had less painwhen moving around ':'gb_moving2',
    'How often patients breathing improved ':'gb_breathing2','How often patients wounds improved or healed after an operation':'gb_wounds_operation2',
    'How often patients had more pressure sores (bed sores) when home health care ended':'patients_moresores',
    'How often patients got better at taking their drugs correctly by mouth ':'gb_medicine2','How often patients got better at taking their drugs correctly by mouth':'gb_medicine2',
    'How often patients receiving home health care needed any urgent unplanned care in the hospital emergency room – without being admitted to the hospital ':'hh_urgentcare_wo_hospitaladmit',
                                              'How often home health patients had to be admitted to the hospital ':'hosp_admit_often',
                                              'How often home health patients had to be admitted to the hospital':'hosp_admit_often',
                                              'Nursing Care':'nc_serv',
                                              'How often the home health team treated their patients pain  ':'hh_treatpain',
                                              'How often patients receiving home health care needed any urgent unplanned care in the hospital emergency room  without being admitted to the hospital ':'hh_urgentcare_wo_hospitaladmit',
                                              'CMS Certification Number (CCN)':'pn',
                                              'Provider Name':'name',
                                              'Address':'address',
                                              'Zip':'zip',
                                              'phone':'phone',
                                              'Phone':'phone',
                                              'Type of Ownership':'owner_type',
                                              'Offers Nursing Care Services':'nc_serv',
                                              'Offers Physical Therapy Services':'pt_serv',
                                              'Offers Occupational Therapy Services':'ot_serv',
                                              'Offers Speech Pathology Services':'sp_serv',
                                              'Offers Medical Social Services':'ms_serv',
                                              'Offers Home Health Aide Services':'hha_serv',
                                              'Date Certified':'date_cert',
                                              'With diabetes how often the home health team got doctors orders gave foot care and taught patients about foot care':'hh_diabetes_footcare',
                                              'How often patients receiving home health care needed urgent unplanned care in the ER without being admitted':'hh_urgentcare_wo_hospitaladmit',
                                              'How often the home health team made sure that their patients have received a flu shot for the current flu season':'hh_fluvax',
                                              'How often the home health team made sure that their patients have received a pneumococcal vaccine (pneumonia shot)':'hh_pneumoniavax',
                                              'Quality of Patient Care Star Rating':'star_rating',
                                              'Quality of patient care star rating':'star_rating',
                                              'How often patients got better at getting in and out of bed':'gb_bed2',
                                              'How often patients breathing improved':'gb_breathing2',
                                              'How often the home health team determined whether patients received a flu shot for the currnet flu season':'hh_fluvax',
                                              'How often the home health team made sure that their patients have received a pneumococcal vaccine (pneumonia shot)':'hh_pneumoniavax',
                                              'Quality of patients care star rating':'star_rating',
                                              'How often home health patients who have had a recent hospital stay received care in the hospital emergency room without being readmitted to the hospital':'hh_urgentcare_wo_hospitalREADMIT',
                                              'How often patients developed new or worsened pressure ulcers':'worse_ulcers',
                                              'How often patients remained in the community after discharge from home health':'community_after_homehealth_discharge',
                                              'How often physician-recommended actions to address medication issues were completely timely':'physician_recommend_timely',
                                              'How much Medicare spends on an episode of care at this agency compared to Medicare spending across all agencies nationally':'medicare_spend_thisagency',
                                              'No of episodes to calc how much Medicare spends per episode of care at agency compared to spending at all agencies (national)':'no_episodes_medicare_spend_thisagency',
                                              'How often the home health team began their patients care in a timely manner':'hh_timely',
                                              'How often the home health team checked  risk of falling':'hh_check_fallrisk',
                                              'With diabetes how often the home health team got doctorâ€™s orders gave foot care and taught patients about foot care':'hh_diabetes_footcare',
                                              'How often  breathing improved':'gb_breathing2',
                                              'How often  wounds improved or healed after an operation':'gb_wounds_operation2',
                                              'DTC Numerator':'dtc_numerator',
                                              'DTC Denominator':'dtc_denominator',
                                              'DTC Observed Rate':'dtc_observedrate',
                                              'DTC Risk-Standardized Rate':'dtc_risk_standardized_rate',
                                              'DTC Risk-Standardized Rate (Lower Limit)':'dtc_risk_standardized_rate_lower_limit',
                                              'DTC Risk-Standardized Rate (Upper Limit)':'dtc_risk_standardized_rate_upper_limit',
                                              'DTC Performance Categorization':'dtc_performance_categorization',
                                              'PPR Numerator':'ppr_numerator',
                                              'PPR Denominator':'ppr_denominator',
                                              'PPR Observed Rate':'ppr_observed_rate',
                                              'PPR Risk-Standardized Rate':'ppr_risk_standardized_rate',
                                              'PPR Risk-Standardized Rate (Lower Limit)':'ppr_risk_standardized_rate_lower_limit',
                                              'PPR Risk-Standardized Rate (Upper Limit)':'ppr_risk_standardized_rate_upper_limit',
                                              'PPR Performance Categorization':'ppr_performance_categorization',
                                              'ZIP':'zip',
                                              'How often the home health team made sure that their patients received a pneumococcal vaccine (pneumonia shot)':'hh_pneumoniavax',
                                              'Changes in skin integrity post-acute care: pressure ulcer/injury':'changes_skin_integrity_ulcer',
                                              'How often home health patients who have had a recent hospital stay had to be re-admitted to the hospital':'hh_hospital_readmit',
                                              'How often home health patients who have had a recent hospital stay received care in the hospital emergency room without being re-admitted to the hospital':'hh_urgentcare_wo_hospitalREADMIT',
                                              'How often the home health team taught patients (or their family caregivers) about their drugs ':'hh_tpatients_drugs',
                                              'How often the home health team checked patients risk of falling ':'hh_check_fallrisk',
                                              'How often the home health team determined whether their patients received a pneumococcal vaccine (pneumonia shot) ':'hh_pneumoniavax',
                                              'How often the home health team began their  care in a timely manner':'hh_timely',
                                              'How often the home health team checked patients for pain':'hh_paincheck',
                                              'How often the home health team treated their patients pain':'hh_treatpain',
                                              'How often the home health team treated heart failure (weakening of the heart) patients symptoms':'hh_treatheart',
                                              'How often the home health team took doctor-ordered action to prevent pressure sores (bed sores)':'hh_doctor_action_sores',
                                              'How often the home health team included treatments to prevent pressure sores (bed sores) in the plan of care':'hh_treatsores',
                                              'How often the home health team checked patients for the risk of developing pressure sores (bed sores)':'hh_check_sores',
                                              'How often the home health team checked patients for depression ':'hh_check_dep',
                                              'How often the home health team determined whether patients received a flu shot for the current flu season ':'hh_fluvax',
                                              'How often patients had less painwhen moving around':'gb_moving2'}
    
    # open file for writing, "w" is writing
    w = csv.writer(open("/Users/aina/Documents/RAProjects/MLTSS/HHA data/data_dictionary.csv", "w"))
    
    # loop over dictionary keys and values
    for key, val in data_dict.items():
        # write every key and value to file
        w.writerow([key, val])
            
    
    #function to rename all columns to shorter, easier phrases (also crucial for concatenating)
    def renamecolumns(each_list):
        for year in range(len(each_list)):
            for quarter in range(len(each_list[0])):
                each_list[year][quarter].rename(columns = data_dict, inplace = True)
        return each_list
    
    #apply function to all lists
    for listitem in [list01, list02, list03, list04]:
        renamecolumns(listitem)          
    
    
    #store unqiue column names in list
    colnameslist = []
    #apply functions to all lists
    for item in [list01, list02, list03, list04]:
        colnames(item, colnameslist)
    colnameslist = uniquecolnames(colnameslist)
       
    #clean up variable explorer
    del item, listitem, df_list, f_list
    
    #store concatenated dataframes here
    dfs = []
    
    #define function to concatenate each year and append it to a holdinglist 
    def concatyear(each_list, holdinglist):
        for list in range(len(each_list)):
            df =  pd.concat(each_list[list])
            holdinglist.append(df)
        return holdinglist
    
    #loop through each list and apply function to concatenate each year of dataframes
    for item in [list01, list02, list03, list04]:
        concatyear(item, dfs)        
    
    #concatenate all years and quarters into one big ass dataframe    
    fulldf = pd.concat(dfs)
    
    #clean up variable explorer
    del dfs, item, list01, list02, list03, list04, key, val, w
    
    #replace mislabeled t columns
    fulldf.loc[fulldf["t"] == 200809, "t"] = 200812
    fulldf.loc[fulldf["t"] == 200909, "t"] = 200912
    fulldf.loc[fulldf["t"] == 201007, "t"] = 201010
    fulldf.loc[fulldf["t"] == 201904, "t"] = 201903
    fulldf.loc[fulldf["t"] == 201907, "t"] = 201906
    fulldf.loc[fulldf['t'] == 202004, "t"] = 202008
    fulldf.loc[fulldf['t'] == 202007, "t"] = 202010
    fulldf.loc[fulldf['t'] == 202101, "t"] = 202107
    fulldf.loc[fulldf['t'] == 202104, "t"] = 202109
    fulldf.loc[fulldf['t'] == 202204, "t"] = 202202
    
    return fulldf

def datacleanup2(df):
    #Because the two files for 2021 are identical, I will drop one. 
    df = df[df.t != 202109]
    
    #count na values for all provider numbers
    df['pn'].isna().sum()
    
    #drop records with na provider numbers, we lose 915 records from this
    df = df[df['pn'].notna()]
    
    #drop records with empty provider numbers, or '\x1a' in the pn field, we lose 25 records from this
    df = df[df['pn'] != '\x1a']
    
    #drop all records with funky provider numbers, we lose 11170 records from this
    df = df[np.core.chararray.find(df.pn.values.astype(str), '=') < 0]
    
    #convert provider numbers to integers
    df.pn = df.pn.astype({'pn':'int'})
    
    return df

fulldf = datacleanup()
fulldf = datacleanup2(fulldf)

#eliminate all providers that do not show up more than once, this loses 74 records
fulldf = fulldf.groupby('pn').filter(lambda x : len(x)>=2)



















