# Task: use apply() to standardise each column of a dataframe

import pandas as pd

# Example code - dataframe.apply()
# Pandas has a built in function to perform this calculation. This will give the bottom 0% to 10% of students the grade 'F', 10% to 20% the grade 'D' and so on
# Read more about this function at http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
if True:
   def convert_grades_curve(exam_grades):
      return pd.qcut(exam_grades,
         [0, 0.1, 0.2, 0.5, 0.8, 1],
         labels = ['F', 'D', 'C', 'B', 'A'])

# qcut() operates on a list, array or series - run it on one of the exams results
print(convert_grades_curve(grades_df['exam1']))

# qcut() does not work on dataframes, but you can use apply() to call the function on each column separately
print(grades_df.apply(convert_grades_curve))


# Rest of task
grades_df = pd.DataFrame(
   data = {'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
      'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
   index = ['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def standardise_column(column):
   return(column - column.mean()) / column.std(ddof = 0)

def standardise(df):
   return df.apply(standardise_column)

standardise(grades_df)
