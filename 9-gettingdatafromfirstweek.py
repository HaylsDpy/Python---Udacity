# Task is to creat a list of rows that includes only paid students and those who did not cancel after the free 7 day trial
# create a function to remove students who cancelled during the free trial

def remove_free_trial_cancels(data):
   new_data = []
   for data_point in data:
      if data_point['account_key'] in paid_students:
         new_data.append(data_point)
   return new_data

# call this function on all 3 tables and save the results in new variables

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

len(paid_enrollments)
len(paid_engagement)
len(paid_submissions)

#Added in from document 12
for engagement_record in paid_engagement:
   if engagement_record['num_courses_visited'] > 0:
      engagement_record['has_visited'] = 1
   else:
      engagement_record['has_visited'] = 0

# find number of paid students from 1st week of data

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
   account_key = engagement_record['account_key']
   join_date = paid_students[account_key]
   engagement_record_date = engagement_record['utc_date']
   if within_one_week(join_date, engagement_record_date):
      paid_engagement_in_first_week.append(engagement_record)

len(paid_engagement_in_first_week)
