# Import a handy function which will read CSV files for us
from csv_handler import read, join_columns

# Read the first year's file
year1 = read('code_club_year_1.csv')
# Read the second year's file
year2 = read('code_club_year_2.csv')

# Create a set of names for each year by merging the first and last name
# set() is the instruction to create a set - this a type used for comparison later
# ''.join(row) says all contents of the row should be joined into a single string
# for row in year1 says that this will be done for each row in the data
year1_names = join_columns(year1)
year2_names = join_columns(year2)

# Of the students attending year 2, this checks which were not in year 1.
new_students = year2_names.difference(year1_names)

# Print all new student's names.
print(sorted(new_students))
