#!/usr/bin/env python
# coding: utf-8

# In[23]:


# PROBLEM 1: Metante_Pandas-P1.py

# Load the corresponding .csv file into a data frame named cars using pandas.

#Start Program

#Importing pandas library
import pandas as pd  

# Loading the .csv file into the data frame
cars = pd.read_csv('cars.csv') 
cars


# In[18]:


# Display the first five rows of the resulting car

cars.head()


# In[20]:


# Display the last five rows of the resulting car

cars.tail()


# In[33]:


# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

a = cars.iloc[:5, 0::2]
a


# In[35]:


# Display the row that contains the ‘Model’ of ‘Mazda RX4’.

b = cars.loc[(cars['Model']=='Mazda RX4 Wag'),]
b


# In[37]:


# How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

c = cars.loc[(cars['Model']=='Camaro Z28'),['Model', 'cyl']]
c


# In[39]:


# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

d = cars.loc[(cars['Model']=='Mazda RX4 Wag') | (cars['Model']=='Ford Pantera L')| (cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
d


# In[ ]:




