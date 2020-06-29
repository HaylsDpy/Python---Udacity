import unicodecsv

with open('/home/hayley/Documents/Data Analysis/enrollments.csv', 'rb') as f:
   reader = unicodecsv.DictReader(f)
   enrollments = list(reader)

print(enrollments [0])

# To open first line of second file
with open('/home/hayley/Documents/Data Analysis/daily_engagement.csv', 'rb') as f:
   reader = unicodecsv.DictReader(f)
   daily_engagement = list(reader)

print(daily_engagement [0])

#to open third file (first line of)
with open('/home/hayley/Documents/Data Analysis/project_submissions.csv', 'rb') as f:
   reader = unicodecsv.DictReader(f)
   project_submissions = list(reader)

print(project_submissions [0])


#arguably better code with the use of a function - NEEDS DEBUGGING
import unicodecsv

def read csv(filename):
   with open(filename, 'rb') as f:
      reader = unicodecsv.DictReader(f)
      return list(reader)

enrollments = read_csv('/home/hayley/Documents/Data Analysis/enrollment.csv')
daily_engagement = read_csv('/home/hayley/Documents/Data Analysis/daily_engagement.csv')
project_submissions = read_csv('/home/hayley/Documents/Data Analysis/project_submissions.csv')

print(enrollments [0])
print(daily_engagement [0])
print(project_submissions [0])
