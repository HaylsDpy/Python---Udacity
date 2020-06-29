# Task: we've created Series containing the various variables we've been looking at this lesson.
# Pick a country you're interested in and make a plot of each variable over time

%pylab inline
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt

employment = pd.read_csv('/home/hayley/Documents/Data Analysis/employment_above_15.csv', index_col = 'Country')
female_completion = pd.read_csv('/home/hayley/Documents/Data Analysis/female_completion_rate.csv', index_col = 'Country')
male_completion = pd.read_csv('/home/hayley/Documents/Data Analysis/male_completion_rate.csv', index_col = 'Country')
life_expectancy = pd.read_csv('/home/hayley/Documents/Data Analysis/life_expectancy.csv', index_col = 'Country')
gdp = pd.read_csv('/home/hayley/Documents/Data Analysis/gdp_per_capita.csv', index_col = 'Country')


employment_us = employment.loc['Brazil']
female_completion_us = female_completion.loc['Brazil']
male_completion_us = male_completion.loc['Brazil']
life_expectancy_us = life_expectancy.loc['Brazil']
gdp_us = gdp.loc['Brazil']

plt.hist(life_expectancy_us)

life_expectancy_us.plot()

# STILL NEED TO SEE WHY SEABORN DOESN'T SEEM TO WORK!!!
