# Task: Previously, you learned how to write code to standardise each column of a DataFrame using apply()
# Standardise each column again, without using apply(), but instead using what you just learned in the previous lesson about adding a DataFrame to a Series

# If you want an extra challenge, trt standardising each ROW of the DataFrame instead, without using apply()

import pandas as pd

# Adding using +
s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
   0: [10, 20, 30, 40],
   1: [50, 60, 70 , 80],
   2: [90, 100, 110, 120],
   3: [130, 140, 150, 160]
})

print(df)
print(df + s)

# Adding with axis = 'index'
# The functions sub(), mul() and div() work similarly to add()
s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
   0: [10, 20, 30, 40],
   1: [50, 60, 70 , 80],
   2: [90, 100, 110, 120],
   3: [130, 140, 150, 160]
})

print(df)
print(df.add(s, axis = 'index'))

# Adding with axis = 'columns'
# The functions sub(), mul() and div() work similarly to add()
s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
   0: [10, 20, 30, 40],
   1: [50, 60, 70 , 80],
   2: [90, 100, 110, 120],
   3: [130, 140, 150, 160]
})

print(df)
print(df.add(s, axis = 'columns'))

#Task
grades_df = pd.DataFrame(
   data = {'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
           'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
   index = ['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

# First, you will need to obtain the mean of each column
grades_df.mean()

# In order to standardise each column, you want to subtract the mean of each column from that column
# I.e. you want to subtract the first mean from every value in the first column and subtract the ssecond mean from every value in the second column
grades_df - grades_df.mean()

# Next, you need to divide each column by its corresponding standard deviation
(grades_df - grades_df.mean()) / grades_df.std()


# So, how would you go about standardising each row?
# This time you will need the mean of each row - using axis = 'columns'
grades_df.mean(axis = 'columns')

# Now you need to subtract the first mean from the first row of the DataFrame, the second mean from the second row and so on
# However, if you try to use the grades_df - grades_df.mean() as you did before, it will try to subract each one of these values from one column of the DataFrame
# Which, actually won't work, as the indexes of this Series don't line up with the column names of the DataFrame
mean_diffs = grades_df.sub(grades_df.mean(axis = 'columns'), axis = 'index')

# Next, to divide by the standard deviation, you need similar code to before
mean_diffs.div(grades_df.std(axis = 'columns'), axis = 'index')
