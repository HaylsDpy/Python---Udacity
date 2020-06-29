# To identify the number of test accounts in the enrollment data set (should = 6)

udacity_test_accounts = set()
for enrollment in enrollments:
   if enrollment['is_udacity']:
      udacity_test_accounts.add(enrollment['account_key'])

len(udacity_test_accounts)

# use function to delete these test accounts from the data set

def remove_udacity_accounts(data):
   non_udacity_data = []
   for data_point in data:
      if data_point['account_key'] not in udacity_test_accounts:
         non_udacity_data.append(data_point)
   return non_udacity_data

# call function on all 3 tables and check how many records are now left

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

len(non_udacity_enrollments)
len(non_udacity_engagement)
len(non_udacity_submissions)
