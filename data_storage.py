# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:44 2024

@author: terre
"""

"""
Storing data inside of python

1. Lists
2. Dictionaryies
3. Data Frames - specific to Pandas
"""


import pandas as pd

file = pd.read_csv("country_data.csv")

print(file)


# dumb way to store the data
age1 = 30
age2 = 25
age3 = 29


# create a list
Age = [39, 25, 29, 46, 22, 35, 22, 49, 30, 40, 30]


print(Age)

# you can mix and match list entries
mix = [5, "tau", 5.99]



# accessing the values inside of the list

# print the first element
print(Age[0])

# print the last element
print(Age[-1])



# you can use build in Python functions to do calculations on the list data

print("The sum of the ages is ",sum(Age))
print("The minimum of the ages is ",min(Age))
print("The maximum of the ages is ",max(Age))


# you can combine the built in functions. E.g. below the average is determined
print("The average of the ages is", sum(Age)/len(Age))





gender = ['M','M','F','M','F','F','F','M','M','F','M']



country = ['South Africa', 'Botswana', 'South Africa', 'South Africa',
           'Kenya', 'Mozambique', 'Lesotho', 'Kenya', 'Kenya', 'Egypt',
           'Sudan']


# you can use array slicing with lists

# print the first three values of the ages
print(Age[:3])

# print the last three age values
print(Age[-3:])


# you can add values to your list
Age.append(100)

print(Age)


# you can insert the values in a list at specific index
# the command below adds the age at the beginning
Age.insert(0, 123)
print(Age)


# you can also remove items from a list
Age.remove(123)

print(Age)

print("\n")



# dictionaries

# a dicitonary is a collection of key valued pairs

mammals = {'cat' : "a cute animal", 'dog':'a loyal animal',
           'lion': "king of the jungle", 'elephant': 'a gigantic herbivore'}

print(mammals)
print('\n')


# you can have a dicitonary with numerical keys
numeric_dict = {1:'one', 2:'two', 3:'three'}
print(numeric_dict)


# you access the dicitonary content by providing the key
print(mammals['cat'])
print('\n')
print(numeric_dict[1])







# Data frames



# creating your own data frame

# you can use a list to create a data frame


fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

size_nm = [9.8, 10.1, 13.2, 8.7, 20.3]


# first make a dicitonary and use the diciotnary to make a data frame
fruit_sizes = {'fruits': fruits,
               'sizes':size_nm}



# create a data frame
df = pd.DataFrame(fruit_sizes)

print(df)
print('\n')


# once the data frame has been created specific columns of it can be accessed
print(df['fruits'])


# you can also use data frame methods to perform functions on certain columns
print(df['sizes'].min())
print(df['sizes'].max())
print(df['sizes'].mean())




# you can also apply array slicing on the data frame
print(df[1:3])

print("\n")

# filter botht he rows and colums
print(df.loc[1:3, 'fruits'])

print("\n")

# you can do filtering
print(df[df['sizes'] > 10])



# you can add other columns or rows to the data frame

prices = [10.00, 12.50, 16.00, 223.00, 7.00]

df['prices'] = prices


# you can remove a column using the drop function

df.drop(columns='prices', inplace=True)



















