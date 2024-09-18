# Experiment 3 - Metante

# I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library.
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library.

# II. Instructions 
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.

++ Download the csv file named 'cars.csv' for the proper demonstration of data analysis.

# PROBLEM 1: Metante_Pandas-P1.py
a. Load the corresponding .csv file into a data frame named cars using pandas.

b. Display the first five and last five rows of the resulting cars.

# Loading the .csv file into the data frame
```
#Start Program

import pandas as pd  #Importing pandas library

cars = pd.read_csv('cars.csv')
cars
```
# Displaying the first five rows of the resulting car
```
cars.head()
```
# Display the last five rows of the resulting car
```
cars.tail()
```


