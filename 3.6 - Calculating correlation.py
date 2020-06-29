# Task: write a function to compute Pearson's r
# Use var.std(ddof = 0) to standardise both x and y. This takes the uncorrected standard deviation - as required for Person's r
import pandas as pd

filename = '/home/hayley/Documents/Data Analysis/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

subway_df.head()


def correlation(x, y):
   std_x = (x - x.mean()) / x.std(ddof = 0)
   std_y = (y -y.mean()) / y.std(ddof = 0)

   return(std_x * std_y).mean()

entries = subway_df['ENTRIESn_hourly']
cumulative_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print(correlation(entries, rain))
print(correlation(entries, temp))
print(correlation(rain, temp))
print(correlation(entries, cumulative_entries))
