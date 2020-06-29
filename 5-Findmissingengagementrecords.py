#run code to find the data for 1 of these students

for enrollment in enrollments:
   student = enrollment['account_key']
   if student not in unique_engagement_students:
      print(enrollment)
      break
