import pandas as import pd

s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index = ['c', 'd', 'e', 'f'])

# NaN = not a number use dropna() to get rid of these
sum_result = s1 + s2

sum_result.dropna()

# Alternate solution: treat missing values as 0 before the addition
s1.add(s2, fill_value = 0)
