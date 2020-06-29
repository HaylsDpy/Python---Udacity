import numpy as np

# output = dtype('int64') which refers to a 64 bit integer
np.array([1, 2, 3, 4]).dtype

enrollments = np.array([
   ['account_key', 'status', 'join_date', 'days_to_cancel', 'is_udacity'],
   [448, 'canceled', '2014-11-10', 65, True],
   [448, 'canceled', '2014-11-05', 5, True],
   [448, 'canceled', '2015-01-27', 0, True],
   [448, 'canceled', '2014-11-10', 0, True],
   [448, 'current', '2015-03-10', np.nan, True]
])


# Pandas data frame

import pandas as pd

enrollments_df = pd.DataFrame({
   'account_key': [448, 448, 448, 448, 448],
   'status': ['canceled', 'canceled', 'canceled', 'canceled', 'current'],
   'join_date': ['2014-11-10', '2014-11-05', '2015-01-27', '2014-11-10', '2015-03-10'],
   'days_to_cancel': [65, 5, 0, 0, np.nan],
   'is_udacity': [True, True, True, True, True]
})

# Have a look at the enrollments dataframe layout
print(enrollments_df)

# Look at the mean of each column within the dataframe
enrollments_df.mean()
