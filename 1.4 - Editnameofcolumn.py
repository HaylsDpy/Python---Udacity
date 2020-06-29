# To edit the name of the 'acct' column in the daily engagement table.
# The other two tables use the name 'account_key', so to make your life easier, rename the odd one to 'account_key' too!

for engagement_record in daily_engagement:
   engagement_record['account_key'] = engagement_record['acct']
   del engagement_record['acct']



def get_unique_students(data):
   unique_students = set()
   for data_point in data:
      unique_students.add(data_point['account_key'])
   return unique_students



#update the previous code to use this function:
unique_enrolled_students = get_unique_students(enrollments)
len(unique_enrolled_students)

unique_enrolled_students = get_unique_students(daily_engagement)
len(unique_engagement_students)

unique_project_submitters = get_unique_students(project_submissions)
len(unique_project_submitters)

#check that the column has, in fact, been changed from 'acct' to 'account_key' (you should get '0' back if it has worked)
print(daily_engagement [0] ['account_key'])



# try these instead to check that 'acct' has actually been deleted (should get an arror when you try to print out the 'acct' one):
# 'account_key' only produces one result though, so maybe this is why the code further down the line isn't working?
len(daily_engagement [0] ['account_key'])

len(daily_engagement [0] ['acct'])
