# EXPERIMENT 3 - Python Data Analysis - Metante

# I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library.
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library.

# II. Instructions 
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.

++ Download the csv file named 'cars.csv' for the proper demonstration of data analysis.

# PROBLEM 1: Metante_Pandas-P1.py
a. Load the corresponding .csv file into a data frame named cars using pandas.

b. Display the first five and last five rows of the resulting cars.
_________________________________________________________________________________________________________________________________________________________
a. Loading the .csv file into the data frame
```
#Start Program

import pandas as pd  #Importing pandas library

cars = pd.read_csv('cars.csv')
cars
```
b. Display the first five rows of the resulting car

```
cars.head()
```
b. Display the last five rows of the resulting car
```
cars.tail()
```
# Full Code Process
```
# PROBLEM 1: Metante_Pandas-P1.py

# Load the corresponding .csv file into a data frame named cars using pandas.

#Start Program

#Importing pandas library
import pandas as pd  

# Loading the .csv file into the data frame
cars = pd.read_csv('cars.csv') 
cars
```
```
# Display the first five rows of the resulting car

cars.head()
```
```
# Display the last five rows of the resulting car

cars.tail()
```
Output:

## cars.head():

<img width="705" height="230" alt="image" src="https://github.com/user-attachments/assets/304f48a5-841d-45ad-8630-2b294539eca8" />

## cars.tail():

<img width="685" height="224" alt="image" src="https://github.com/user-attachments/assets/dadd2ba4-fe33-456c-af04-a23030bb74a6" />


# PROBLEM 2: Metante_Pandas-P2.py
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

_________________________________________________________________________________________________________________________

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
```
a = cars.iloc[:5, 0::2]
a
```

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
```
b = cars.loc[(cars['Model']=='Mazda RX4 Wag'),]
b
```

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
```
c = cars.loc[(cars['Model']=='Camaro Z28'),['Model', 'cyl']]
c

```

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

```
d = cars.loc[(cars['Model']=='Mazda RX4 Wag') | (cars['Model']=='Ford Pantera L')| (cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
d
```

# Full Code Process

```
# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

a = cars.iloc[:5, 0::2]
a

# Display the row that contains the ‘Model’ of ‘Mazda RX4’.

b = cars.loc[(cars['Model']=='Mazda RX4 Wag'),]
b

# How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

c = cars.loc[(cars['Model']=='Camaro Z28'),['Model', 'cyl']]
c

# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

d = cars.loc[(cars['Model']=='Mazda RX4 Wag') | (cars['Model']=='Ford Pantera L')| (cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
d
```

Output:

## First five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

<img width="412" height="223" alt="image" src="https://github.com/user-attachments/assets/6e4c0bfb-22a8-41f7-8ed6-b6d2ad5b32fc" />

##  Row that contains the ‘Model’ of ‘Mazda RX4’.

<img width="695" height="65" alt="image" src="https://github.com/user-attachments/assets/ffe013b4-3624-49df-af86-b0b43d9f79c6" />

## How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

<img width="185" height="76" alt="image" src="https://github.com/user-attachments/assets/a441c85c-cc62-45ed-9a08-b1473e7932e0" />

## How many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

<img width="273" height="140" alt="image" src="https://github.com/user-attachments/assets/54b0b01c-195e-41f0-bdad-dd2a6b58e24b" />

# That's all. Thanks :)

Marc Gabriel G. Metante - UST ECE












