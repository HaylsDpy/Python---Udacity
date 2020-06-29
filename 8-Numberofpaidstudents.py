# Question: How do numbers in the daily engagement table differ for students who pass the first project, vs those whoe don't?
# Find the number of students who paid for their course, whilst only looking at the data from the first week. Include students
# who haven't cancelled yet, stayed enrolled for more than 7 days (eliminates users who only stuck around for the 7 day free trial)

# students can enroll multiple times, so only use most recent enrollment date - saves saving the multiple student twice in the the dictionary
# you are creating below


paid_students = {}
for enrollment in non_udacity_enrollments:
   if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
      account_key = enrollment['account_key']
      enrollment_date = enrollment['join_date']
      if account_key not in paid_students or enrollment_date > paid_students[account_key]:
         paid_students[account_key] = enrollment_date

len(paid_students)

# To get students whose engagement lasted one week or more

def within_one_week(join_date, engagement_date):
   time_delta = engagement_date - join_date
   return time_delta.days < 7 and time_delta.days >= 0
