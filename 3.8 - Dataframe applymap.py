# Task: convert numerical grades to letter grades using applymap to creat a new data frame from the one already provided

import pandas as import pd

grades_df = pd.DataFrame(
   data = {'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
      'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
   index = ['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grade(grades):
   if grades >= 90:
      return 'A'
   elif grades >= 80:
      return 'B'
   elif grades >= 70:
      return 'C'
   elif grades >= 60:
      return 'D'
   else:
      return 'F'

def convert_grades(grades):
   return grades.applymap(convert_grade)

print(convert_grades(grades_df))
