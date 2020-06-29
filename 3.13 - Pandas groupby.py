# Task: group the subway data by a variable of your choice - day of the week/ hour of the day/ whether it was raining or not. Then, find the mean subway ridership for
# each different value and either, produce a plot showing the results, or, simply print out the numbers, if that makes more sense.

%pylab inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
   'value': values,
   'even': values % 2 == 0,
   'above_three': values > 3},
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
)

# Example code:
# Examine DataFrame
print(example_df)

# Examine groups
grouped_data = example_df.groupby('even')
print(grouped_data.groups)

# Group by multiple coulmns
grouped_data = example_df.groupby(['even', 'above_three'])
print(grouped_data.groups)

# Get the sum of each group
grouped_data = example_df.groupby('even')
print(grouped_data.sum())

# Limit columns in result
grouped_data = example_df.groupby('even')
# You can take one of more columns from the resulting DataFrame
print(grouped_data.sum()['value'])
# You can also take a subset of columns from the grouped data before collapsing to a DataFrame. In this case, the result is the same.
print(grouped_data['value'].mean())


# Rest of task
filename = '/home/hayley/Documents/Data Analysis/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

subway_df.head()

# Group data by day of the week and produce a plot
subway_df.groupby('day_week').mean()['ENTRIESn'].plot()

# Group data by day of the week and hourly entries
subway_df.groupby('day_week').mean()['ENTRIESn_hourly'].plot()
