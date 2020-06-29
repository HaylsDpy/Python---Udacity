# Task: previously, you had calculated entires and exits on a cumulative basis. In this task, write a function to correctly calculate the hourly entries and exits.
# Use the apply() function to call the function that you wrote previously. You should also make sure you restrict your grouped data to just the entries and exits columns,
# since your function may cause an error if it is called on non-numerical data types.

import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
   'value': values,
   'even': values % 2 == 0,
   'above_three': values > 3},
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
)

# Example code:
# Standardise each group
def standardise(xs):
   return (xs - xs.mean()) / xs.std()
   grouped_data = example_df.groupby('even')

print(grouped_data['value'].apply(standardise))

# Find second largest value in each group - DEBUG
def second_largest(xs):
   sorted_xs = xs.sort(inline = False, ascending = False)
   return sorted_xs.iloc[1]
   grouped_data = example_df.groupby('even')

print(grouped_data['value'].apply(second_largest))

# Rest of task:
# DataFrame with cumulative entired and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def hourly_for_group(entries_and_exits):
   return entries_and_exits - entries_and_exits.shift(1)

ridership_df.groupby('UNIT')[['ENTRIESn', 'EXITSn']].apply(hourly_for_group)
