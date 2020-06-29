# Task: create a plot of your choise using the NP subway data
%pylab inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Example code:
values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# groupby() without as_index
first_even = example_df.groupby('even').first()

print(first_even)
print(first_even['even'])  # Causes an error as 'even' is no longer a column in the DataFrame

# groupby() with as_index = False
first_even = example_df.groupby('even', as_index = False).first()

print(first_even)
print(first_even['even']) # Now 'even' is still a column in the DataFrame


# Rest of Task:
filename = '/home/hayley/Documents/Data Analysis/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

# Make a scatterplot of subway stations with latitude and longitude as the x and y axes and ridership as the bubble size
data_by_location = subway_df.groupby(['latitude', 'longitude'], as_index = False).mean()
#Have a look at the first few rows of this:
data_by_location.head()

# Now, extract the longitude and latitude from the DataFrame.
# latitude and longitude are no longer columns in this DataFrame - instead, they've been transformed into the row indexes for the DataFrame. Add 'groupby() False' to the data_by_location function to remedy this
data_by_location.head()['latitude']

# Next, create the scatterplot with latitude as the x coordinates, and longitude as the y coordinates
# (This works to create a scatterlot of all the subway stations, but you haven't yet made the bubble size dependent on the ridership)
plt.scatter(data_by_location['latitude'], data_by_location['longitude'])

# Add on code to determine the size of each bubble
plt.scatter(data_by_location['latitude'], data_by_location['longitude'], s = data_by_location['ENTRIESn_hourly'])



# It looks like te previous code worked, but the bubbles are so big that it makes the plot really difficult to read or understand
# To account for this, make a new variable that divides each entiry the by standard deviation
scaled_entries = (data_by_location['ENTRIESn_hourly'] / data_by_location['ENTRIESn_hourly'].std())
# Then change the size argument to the scatterplot function to be the scaled entries, rather than the raw entries
plt.scatter(data_by_location['latitude'], data_by_location['longitude'], s = scaled_entries)
