import numpy as np

# Using index arrays
if True:
   a = np.array([1, 2, 3, 4])
   b = np.array([True, True, False, False])

   print(a[b])
   print(a[np.array([True, False, True, False])])

# Creating the index array using vectorised operations
if True:
   a = np.array([1, 2, 3, 2, 1])
   b = (a >= 2)

   print(a[b])
   print(a[a >= 2])

# Creating the index array using vectorised operations on another array
if True:
   a = np.array([1, 2, 3, 4, 5])
   b = np.array([1, 2, 3, 2, 1])

   print(b == 2)
   print(a[b == 2])

# Time spent in the classroom in the first week for 20 students
time_spent = np.array([10, 10, 10, 60, 60, 60])

# Days to cancel for 20 students
days_to_cancel = np.array([5, 5, 5, 10, 10, 10])

def mean_time_for_paid_students(time_spent, days_to_cancel):
   return time_spent[days_to_cancel >= 7].mean()

print(mean_time_for_paid_students(time_spent, days_to_cancel))
