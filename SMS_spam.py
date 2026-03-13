import pandas as pd

# loading the sms dataset
data = pd.read_csv("spam.csv", encoding="latin-1")

# printing the first rows of the dataset

print(data.head())

# Exporing the data

print(data.shape)

# Generating informantion about the data set
data.info()


