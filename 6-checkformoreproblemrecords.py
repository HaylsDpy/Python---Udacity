#run code to check for 'problem entries' - anomalies between the number of students who enrolled vs the number of students who actually attended classes (engaged)
# output should be 3

num_problem_students = 0

for enrollment in enrollments:
   student = enrollment['account_key']
   if student not in unique_engagement_students and enrollment['join_date'] != enrollment['cancel_date']:
      num_problem_students += 1

print(num_problem_students)
