# DataFrames are a great data structure to represent CSVs

import pandas as pd

subway_df = pd.read_csv('/home/hayley/Documents/Data Analysis/nyc_subway_weather.csv')

# To print out a small part of the file (first 5 lines), use the head() function
subway_df.head()

# Use the describe() function to find out some info about each column
subway_df.describe()
