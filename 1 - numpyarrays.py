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

# Change False to True for each block of code to see what it does #

# Accessing elements (should return Afghanistan and Angola)
if True:
   print(countries[0])
   print(countries[3])

# Slicing
if True:
   print(countries[0:3])
   print(countries[:3])
   print(countries[17:])
   print(countries[:])

# Element types
if True:
   print(countries.dtype)
   print(employment.dtype)
   print(np.array([0, 1, 2, 3]).dtype)
   print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
   print(np.array([True, False, True]).dtype)
   print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)

# Looping
for country in countries:
   print('Examining country:', country)

for i in range(len(countries)):
   country = countries[i]
   country_employment = employment[i]
   print('Country:', str(country), 'has employment:', str(country_employment))



#OR - teacher's version (not flawless)
for country in countries:
   print('Examining country {}'.format(country))

for i in range(len(countries)):
   country = countries[i]
   country_employment[i]
   print('Country {} has employment {}'.format(country, country_employment))

# Numpy functions
if True:
   print(employment.mean())
   print(employment.std())
   print(employment.max())
   print(employment.sum())

def max_employment(countries, employment):
   country = None
   country_employment = 0
   for i in range(len(countries)):
      if employment[i] == employment.max():
         country = countries[i]
         country_employment = employment[i]
         break
   return(country, country_employment)

max_employment(countries, employment)
