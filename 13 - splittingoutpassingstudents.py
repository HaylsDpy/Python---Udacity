# Find all students who passed their first project (should = 647)

subway_project_lesson_keys = ['746169184', '3176718735']
pass_subway_project = set()

for submissions in paid_submissions:
   if submissions['lesson_key'] in subway_project_lesson_keys:
      if submissions['assigned_rating'] == 'PASSED' or submissions['assigned_rating'] == 'DISTINCTION':
         pass_subway_project.add(submissions['account_key'])

len(pass_subway_project)

# Split data into those who passed and those who didn't (should = 4527 and 2392)

passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_engagement_in_first_week:
   if engagement_record['account_key'] in pass_subway_project:
      passing_engagement.append(engagement_record)
   else:
      non_passing_engagement.append(engagement_record)

len(passing_engagement)
len(non_passing_engagement)
