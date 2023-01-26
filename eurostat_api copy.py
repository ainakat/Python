#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 12:50:31 2022

@author: aina
"""

#****************#
#***Malieka debugging***#

##check current version of pip
#pip --version

#upgrade pip to current version (pip 22.3.1)
#pip install --upgrade pip

#install for malieka's computer
##pip install eurostat


#allows us to manipulate data as a dataframe
import pandas as pd


#import python package designed for eurostat data 
import eurostat as eurostat

#apri_ap_crpouta API CALL
#specify parameters for data pull
filter_pars = {'CURRENCY': ['EUR'],
               'FREQ': ['A'],
               'GEO': ['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK'],
               'PROD_VEG': ['01110000','01300000','01500000','01910000','02110000','02120000','02130000']}

#pull apri_ap_crpouta data given the filter_pars specified above
apri_ap_crpouta = eurostat.get_sdmx_data_df('apri_ap_crpouta', 2000, 2001, filter_pars, flags = False, verbose=True)




#apri_pi15_outa API CALL
#specify parameters for data pull
filter_pars = {'P_ADJ': ['NI'],
               'FREQ': ['A'],
               'GEO': ['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK'],
               'UNIT': ['I15'],
               'PRODUCT': ['010000','011100','013000','015000','021100','021200','021300']}

#pull apri_ap_crpouta data given the filter_pars specified above
apri_pi15_outa = eurostat.get_sdmx_data_df('apri_pi15_outa', 2000, 2021, filter_pars, flags = False, verbose=True)





#apri_pi15_outq API CALL
#specify parameters for data pull
filter_pars = {'FREQ': ['Q'],
               'GEO': ['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK'],
               'UNIT': ['I15'],
               'PRODUCT': ['010000','011100','013000','015000','021100','021200','021300'], 
               'P_ADJ': ['NI'] }

#pull apri_ap_crpouta data given the filter_pars specified above
apri_pi15_outq = eurostat.get_sdmx_data_df('apri_pi15_outq', 2000, 2021, filter_pars, flags = False, verbose=True)





#apro_cpsh1 API CALL
#specify parameters for data pull
filter_pars = {'FREQ': ['A'],
               'GEO': ['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK'],
               'CROPS': ['C1110', 'C1300','C1500','C1700','I1110','I1120','I1130'],
               'STRUCPRO': ['PR_HU_EU']}

#pull apri_ap_crpouta data given the filter_pars specified above
apro_cpsh1 = eurostat.get_sdmx_data_df('apro_cpsh1', 2000, 2021, filter_pars, flags = False, verbose=True)



############
############THIS NEEDS TO BE ADJUSTED FOR MALIEKA'S DESKTOP LOCATION
############

# Create a Pandas Excel writer using XlsxWriter as the engine.
#writer = pd.ExcelWriter('/Users/aina/Desktop/eurostat_API2.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
#apri_ap_crpouta.to_excel(writer, sheet_name='apri_ap_crpouta')
#apri_pi15_outa.to_excel(writer, sheet_name='apri_pi15_outa')
#apri_pi15_outq.to_excel(writer, sheet_name='apri_pi15_outq')
#apro_cpsh1.to_excel(writer, sheet_name='apro_cpsh1')


# Close the Pandas Excel writer and output the Excel file.
#writer.save()
