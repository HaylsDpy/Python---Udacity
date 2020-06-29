# To find the number of enrollments

len(enrollments)

# To find the number of unique students who enrolled - add account keys to a set, then look at the length of the set

unique_enrolled_students = set()
for enrollment in enrollments:
   unique_enrolled_students.add(enrollment['account_key'])

len(unique_enrolled_students)

# Number of entries in daily engagement table

len(daily_engagement)

unique_engagement_students = set()
for engagement_record in daily_engagement:
   unique_engagement_students.add(engagement_record['acct'])

len(unique_engagement_students)

# For project submissions

len(project_submissions)

unique_project_submitters = set()
for submission in project_submissions:
   unique_project_submitters.add(submission['account_key'])

len(unique_project_submitters)
