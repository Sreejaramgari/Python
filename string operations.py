s = "Codegnan"
print(s[0:5:1])
print(s[6:10])
print(s[5:8:-1])
print(s[0:5])
print(s[::-1])
print(s[::2])

#attendance management system
n = 5
absent = 0
present = 0
for i in range(1, n+1):
    val = int(input(f"Enter Roll no {i} attendance (0 = absent, 1 = present): "))
    if val == 1:
        present += 1
    else: 
        absent += 1
        percentage = (present / n) * 100
print("Total Students:", n)
print("Total Present:", present)
print("Total Absent:", absent)
print("Attendance Percentage:", percentage, "%")
