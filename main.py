# First start importing pandas library
import pandas as pd

# Second convert the csv file with the data into a dataframe
schools = pd.read_csv('schools.csv')

#3 Third by default pycharm does not allow you to see each row and column in the dataFrame
#3 for data set some important options in order to display the information

# Display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

