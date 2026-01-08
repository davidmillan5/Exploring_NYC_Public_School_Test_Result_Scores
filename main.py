# First start importing pandas, matplotlib and numpy libraries
import pandas as pd
import matplotlib.pylab as plt
import numpy as np

# Second convert the csv file with the data into a dataframe
filename = 'schools.csv'
schools = pd.read_csv(filename)

# Third by default pycharm does not allow you to see each row and column in the dataFrame
# for data set some important options in order to display the information

# Fourth  Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Fifth verify that the dataframe was successfully created
# .head() print the first 5 rows on the table
print('=========   Headers (.head())   ======')
print(schools.head())

# Sixth Print a concise summary of a DataFrame. using .info function
print('=========   Summary (.info)   ======')
print(schools.info())

# Seventh Generate descriptive statistics.

# Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution,
# excluding NaN values.
print('=========   Descriptive Statistics (.describe())   ======')
print(schools.describe())

# Eight Generate Explore the column Labels.
print('=========   Columns Labels (.columns())   ======')
print(schools.columns)

# Ninth Return the dtypes in the DataFrame.
print('=========   Type of each column (.dtypes)   ======')
print(schools.dtypes)


#Tenth Evaluate for missing values
missing_data = schools.isnull().sum()
print(missing_data)
# print(missing_data.head(10))

### Hands On

# Which NYC schools have the best math results?
#
# The best math results are at least 80% of the *maximum possible score of 800* for math.
# Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns,
# sorted by "average_math" in descending order.
#

math_max = 800
best_math_results = 800 * 0.80
print(best_math_results)

print('========   Best Math Schools ===============')
best_math_schools = schools[schools['average_math'] >= best_math_results].sort_values(by=['average_math'], ascending=False)
print(best_math_schools[['school_name', 'average_math']])
print('========   Best Math Schools ===============')




