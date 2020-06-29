import pandas as import pd

# Additions when indexes are the same
if True:
   s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
   s2 = pd.Series([10, 20, 30, 40], index = ['a', 'b', 'c', 'd'])

   print(s1 + s2)

# Indexes have same elements in different order
if True:
   s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
   s2 = pd.Series([10, 20, 30, 40], index = ['b', 'd', 'a', 'c'])

   print(s1 + s2)

# Indexes overlap, but do not have exactly the same elements
if True:
   s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
   s2 = pd.Series([10, 20, 30, 40], index = ['c', 'd', 'e', 'f'])

   print(s1 + s2)

# Indexes that do not overlap
if True:
   s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
   s2 = pd.Series([10, 20, 30, 40], index = ['e', 'f', 'g', 'h'])

   print(s1 + s2)
