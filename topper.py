# this file main aim is to find topper

# 1. read total number of students
total_students = int(input("Enter total number of students: "))

# for storing each student's marks
telugu_marks = []
english_marks = []
hindi_marks = []
maths_marks = []
science_marks = []
social_marks = []
total_marks = []   # storing each student total marks
students_names = []   # stores students names

for i in range(total_students):
    # read student name
    name = input("Enter student name: ")

    # read marks
    telugu, english, hindi, maths, science, social = map(
        int, input("Enter marks (Telugu English Hindi Maths Science Social): ").split()
    )

    # add marks to lists
    telugu_marks.append(telugu)
    english_marks.append(english)
    hindi_marks.append(hindi)
    maths_marks.append(maths)
    science_marks.append(science)
    social_marks.append(social)
    students_names.append(name)

    # calculate total
    total = telugu + english + hindi + maths + science + social
    total_marks.append(total)

# find maximum marks
max_marks = max(total_marks)

# find topper indexes
topper_indices = []
for i in range(total_students):
    if total_marks[i] == max_marks:
        topper_indices.append(i)

# print topper details
print("\nTopper Details:")
for index in topper_indices:
    print("Name:", students_names[index])
    print("Total Marks:", total_marks[index])