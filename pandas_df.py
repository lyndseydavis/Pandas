import pandas as pd

pd.set_option("precision", 2)

# data frames are two dimensional (like a table)
# series are one dimensional
# each column of a df is a series


grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

# change row index to custom
grades.index = ["Test 1", "Test 2", "Test 3"]

# print(grades)

eva = grades["Eva"]
sam = grades.Sam

# using loc and iloc methods
test2 = grades.loc["Test 2"]
test1 = grades.iloc[0]

# consecutive rows
test1_thru_3 = grades.loc["Test 1":"Test3"]

# nonconsecutive rows -- index needs to be in a list inside the outer brackets
test1_and_test3 = grades.loc[["Test 1", "Test 3"]]

test1_and_test2 = grades.iloc[
    0:2
]  ##does not include upper row so to get both tests need to actually do 0:2, loc easier than iloc


# Eva and Katies grades for Test 1 and Test2
eva_and_katie = grades.loc[:"Test 2", ["Eva", "Katie"]]

# sam thru bob grades for test 1 and test 3
sam_thru_bob = grades.loc[["Test 1", "Test 3"], "Sam":]

# boolean indexing
# selecting everyone with an A, B, or AorB grade
grades_A = grades[grades >= 90]
grades_B = grades[(grades >= 80) & (grades < 90)]
grades_A_or_B = grades[(grades >= 90) | (grades >= 80)]


# by student
print(grades.describe())
# by test
print(grades.T.describe())
# average grades for each test
print(grades.T.mean())

# sort row by index (test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

# sorty by column  name
c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)

print()
