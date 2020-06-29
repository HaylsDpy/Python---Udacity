
# Next, the instructor starts looking to debug the code. She finds that the number of minutes spent by any student during the first week is actually greater than the number of
# minutes in a week. To investigate this, she searches for the student with the maximum number of minutes in the engagement data.

# First, use this code to find the total minutes

# Import library
from collections import defaultdict

# Creates a dictionary of engagement grouped by student
# The keys are account keys, and the values are lists of engagement records.
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)
#    total_minutes = total_minutes_by_account.values()

# Creates a dictionary with the total minutes each student spent in the classroom during the first week
# The keys are account keys, and the values are numbers (total minutes)
total_minutes_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes


#Import library
# Summarize the data about minutes spent in the classroom
import numpy as np

total_minutes = total_minutes_by_account.values()

print('Mean:', np.mean(list(total_minutes)))
print('Standard deviation:', np.std(list(total_minutes)))
print('Minimum:', np.min(list(total_minutes)))
print('Maximum:', np.max(list(total_minutes)))


# Find the student with the most minutes in the engagement data
# Locates at least one surprising piece of data and outputs it
student_with_max_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
   if total_minutes > max_minutes:
      max_minutes = total_minutes
      student_with_max_minutes = student

print('Max minutes:', max_minutes)

# Print each engagement record for that student

for engagement_record in paid_engagement_in_first_week:
   if engagement_record['account_key'] == student_with_max_minutes:
      print('Engagement record:', engagement_record)

### This would result in way more than the 7 entries that you are looking for. This shouldn't be the case since it's within the 'engagement in first week' dictionary.
### The data points were not in the first week either - massive variation in dates.
### SO - the 'within one week' function was edited to account for this (look back in file number 8)
### This should account for the number of engagement data hours being over the number of hours in a week
### Should result in exactly 7 entries when printing out the engagement date for that 1 student
