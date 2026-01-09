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
#print(best_math_results)

#print('========   Best Math Schools ===============')
best_math_schools_prev = schools[schools['average_math'] >= best_math_results].sort_values(by=['average_math'], ascending=False)
best_math_schools = best_math_schools_prev[['school_name', 'average_math']]
print('========   Best Math Schools ===============')
print(best_math_schools)
print('========   Best Math Schools ===============')
print(best_math_schools[['school_name', 'average_math']].set_index('school_name'))
#print('========   Best Math Schools ===============')

# What are the top 10 performing schools based on the combined SAT scores?
#
# Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT",
# with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).

columns_to_sum = ['average_math', 'average_reading', 'average_writing']
schools['total_SAT'] = np.sum(schools[columns_to_sum], axis=1)

print("\nDataFrame with new 'total_SAT' column:")
print(schools.sort_values(by=['total_SAT'],ascending=False))


print('========   top_10_schools   ===============')
top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by=['total_SAT'],ascending=False).head(10)
print(top_10_schools)



# Which single borough has the largest standard deviation in the combined SAT score?
#
# Save your results as a pandas DataFrame called largest_std_dev.
# The DataFrame should contain one row, with:
# "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
# "num_schools" - the number of schools in the borough.
# "average_SAT" - the mean of "total_SAT".
# "std_SAT" - the standard deviation of "total_SAT".
# Round all numeric values to two decimal places.


print("========================== Schools ============================")
print(schools.head(10))

#print(schools.groupby('borough')['total_SAT'].std().round(2).max())
schools['largest_std_total_std'] = schools['total_SAT'].std().round(2).max()
#print(schools.groupby('borough')['school_name'].nunique())
schools['num_schools'] = schools.groupby('borough')['school_name'].transform('count')
#print('num_schools', schools['num_schools'])
schools['average_SAT'] = schools['total_SAT'].mean().round(2)
schools['std_SAT'] = schools['total_SAT'].std().round(2)
#print(schools.head())
#

largest_std_dev = (
    schools
    .groupby("borough")
    .agg(
        num_schools=("borough", "count"),
        average_SAT=("total_SAT", "mean"),
        std_SAT=("total_SAT", "std")
    )
    .round(2)
    .sort_values("std_SAT", ascending=False)
    .head(1)
)

print(largest_std_dev)
