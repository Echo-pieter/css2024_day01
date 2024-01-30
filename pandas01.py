# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:27:09 2024

@author: terre
"""

import pandas as pd
import numpy as np

file = pd.read_csv("country_data.csv")

# print(file)


# the .info command gives information regarding the file variable
# print(file.info())

# the .describe command gives describe statistics for the dataframe
# print(file.describe())







# teh .info and .describe commands will be used on the other csv files
file_diab = pd.read_csv("diab_data.csv")

#display the diab_data file
# print(file_diab)


# get information regarding the diab_data file
# print(file_diab.info())

# get stats regarding the diab_data file
# print(file_diab.describe())







# this file had no headings

file_house = pd.read_csv("housing_data.csv")

# display the housing_data file

print(file_house)


# get info regarding the housing_data file
#print(file_house.info())


# get stats regarding the housing_data file
# print(file_house.describe())


# give it colum headings
column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

c = np.arange('N')


# give it new column names
file_house = pd.read_csv("housing_data.csv", names=column_names)


print(file_house)






# had a bunch of text before the column headings, had to skip them

file_insurance = pd.read_csv("insurance_data.csv", skiprows=6)


# display the insurance_data.csv file
# print(file_insurance)

# display the info of the insurance data
# print(file_insurance.info())


# get the stat description of the insurance data
# print(file_insurance.describe())





file_iris = pd.read_csv("iris.csv")


#print the iris data
# print(file_iris)


# get the info of the iris data
# print(file_iris.info())


# get the stats of the iris data
#print(file_iris.describe())



