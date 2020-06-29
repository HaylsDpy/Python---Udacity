#Adapt code to analyse lessons completed instead of minutes spent (try to write a function, rather than copying and pasting the code)

from collections import defaultdict

def group_data(data, key_name):
   grouped_data = defaultdict(list)
   for data_point in data:
      key = data_point[key_name]
      grouped_data[key].append(data_point)
   return grouped_data

#---

def sum_grouped_items(grouped_data, field_name):
   summed_data = {}
   for key, data_points in grouped_data.items():
      total = 0
      for data_point in data_points:
         total += data_point[field_name]
      summed_data[key] = total
   return summed_data


# refer to document 15 and notes in notebook for further explanation
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def describe_data(data):
   print('Mean:', np.mean(list(data)))
   print('Standard Deviation:', np.std(list(data)))
   print('Minimum:', np.min(list(data)))
   print('Maximum:', np.max(list(data)))
   plt.hist(data)

engagement_by_account = group_data(paid_engagement_in_first_week, 'account_key')
lessons_completed_by_account = sum_grouped_items(engagement_by_account,'lessons_completed')
describe_data(lessons_completed_by_account.values())



# Results should be the same as before for the above function

#For this, the result was a mean of around 1.636, SD of 3.00, min of 0 and max of 36



## This is the version found in github
%pylab inline
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def describe_data(data, title):
   print('Mean:', np.mean(list(data)))
   print('Standard Deviation:', np.std(list(data)))
   print('Minimum:', np.min(list(data)))
   print('Maximum:', np.max(list(data)))
   plt.hist(list(data), bins=8)
   plt.xlabel('Number of days')
   plt.title(title)

engagement_by_account = group_data(paid_engagement_in_first_week, 'account_key')
lessons_completed_by_account = sum_grouped_items(engagement_by_account,'lessons_completed')
describe_data(lessons_completed_by_account.values(), 'Distribution of classroom visits in the first week')
