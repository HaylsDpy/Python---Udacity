import numpy as np

# First 20 countries with employment data
countries = np.array([
   'Afghanistan', 'Albania', 'Algeria', 'Angola',
   'Argentina', 'Armenia', 'Australia', 'Austria',
   'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
   'Barbados', 'Belarus', 'Belgium', 'Belize',
   'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
     55.70000076, 51.40000153, 50.5, 75.69999695,
     58.40000153, 40.09999847, 61.5, 57.09999847,
     60.90000153, 66.59999847, 60.40000153, 68.09999847,
     66.90000153, 53.40000153, 48.59999847, 96.79999924,
     71.59999847, 58.40000153, 70.40000153, 41.20000076
  ])

# Change this country name to change what country will be printed when you click 'test run'. Your function will be called to determine the standardised score for this
# country for each of the given 5 Gapminder variables in 2007. The possible country names are available in the Downloadables section in Udacity.

country_name = 'United States'

# Process is: calculating the distance of a given value from the mean (values - values.mean()), then to convert to a number of standar deviations, divide by the SD (/ values.std())
# 'values' refers to the entire array
# values - values.mean() subtracts the mean from each value in the array
# / values.std() divides each element in the array by the standard deviation

def standardised_data(values):
   return(values - values.mean()) / values.std()

print(standardised_data(employment))
