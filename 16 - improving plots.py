# utilise the seaborn library (can be added to your describe_data function in doc 11)
# import seaborn as sns

import seaborn as sns

plt.hist(passing_visits.values(), bins= 8)
plt.xlabel('Number of days')
plt.title('Distribution of classroom visits in the first week' + 'for students who pass the subway project')


plt.hist(non_passing_visits.values(), bins = 8)
plt.xlabel('Number of days')
plt.title('Distribution of classroom visits in the first week' + 'for students who do not pass the subway project')
