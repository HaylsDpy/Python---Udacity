# Task: write code to return the second largest value of each column of the input DataFrame (df)

import numpy as np
import pandas as pd

df = pd.DataFrame({
   'a': [4, 5, 3, 1, 2],
   'b': [20, 10, 40, 50, 30],
   'c': [25, 20, 5, 15, 10]
})

# DataFrame apply() for case 2
if True:
   print(df.apply(np.mean))
   print(df.apply(np.max))

# Pandas sort_values() function - pass ascending as False so that the Series is sorted in descending order (amakes more sense as we are trying to determine the second LARGEST number)
def second_largest_in_column(df):
   sorted_column = df.sort_values(ascending = False)
   return sorted_column.iloc[1]

# check to see if this function works by calling it on one of the columns in the DataFrame
second_largest_in_column(df['a'])

# Now use apply() to use this function on the whole DataFrame
def second_largest(df):
   return df.apply(second_largest_in_column)

# Print the results
print(second_largest(df))
