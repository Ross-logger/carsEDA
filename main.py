import pandas as pd

cars = pd.read_csv('/Users/admin/PycharmProjects/carsEDA/data/file.csv')

# print(cars.head())

# checking where we have null value
null_counts = cars.isnull().sum()

# Task 1: we will fill null values with the mean of that column if it is a number
for column in null_counts.index:
    if null_counts[column] > 0:
        if cars[column].dtype.kind in 'biufc':
            cars[column] = cars[column].fillna(cars[column].mean())

print(cars.isnull().sum())

# Task 2: to show the number of cars of every Make
print(cars['Make'].value_counts())

# Task 3: to show the cars from Asia and Europe countries
print(cars[cars['Origin'].isin(['Asia', 'Europe'])])

# Task 4: to remove the records where the weight is larger than 4000
print(cars[~(cars['Weight'] > 4000)])

# Task 5: to increase each value of "MPG_City" column by value 3

cars = cars['MPG_City'].apply(lambda x: x + 3)
print(cars)
