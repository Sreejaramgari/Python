#Find weather the number is positive even,negative even,positive odd,negative odd
a = int(input("Enter a number: "))
if a >= 0 and a % 2 == 0:
    print("positive even")
elif a < 0 and a % 2 == 0:
    print("negative even")
elif a >= 0 and a % 2 != 0:
    print("positive odd")
elif a < 0 and a % 2 != 0:
    print("Negative odd")
else:
    print("Invalid")

#Find biggest of 3 numbers
n1 = int(input("Enter a num: "))
n2 = int(input("Enter a num: "))
n3 = int(input("Enter a num: "))
if n1 >= n2 and n1 >= n3:
    print(n1, "n1 is greater: ")
elif n2 >= n1 and n2 >= n3:
    print(n2, "n2 is greater: ")
elif n3 >= n1 and n3 >= n2:
    print(n3, "n3 is greater: ")
else:
    print("invalid")

#
n1 = int(input("Enter a num: "))
n2 = int(input("Enter a num: "))
n3 = int(input("Enter a num: "))
if n1 > n2 and n1 > n3:
    print(n1, "n1 is greater: ")
elif n2 > n3:
    print(n2, "n2 is greater: ")
else:
    print(n3, "n3 is greater: ")

#find the biggest of three numbers where 2 equal numbers,3 equal numbers and 3 different numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b == c:
    print("All three numbers are equal")
elif a == b and a > c:
    print("a and b are equal and a is greater")
elif b == c and b > a:
    print("b and c are equal and b is greater")
elif a == c and a > b:
    print("a and c are equal and a is greater")
elif a > b and a > c:
    print("a is the greater")
elif b > a and b > c:
    print("b is the greater")
else:
    print("c is the greater")

#find the biggest of 3 numbers using nested if condition
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("a is the greater")
    else:
        print("c is the greater")
else:
    if b > c:
        print("b is the greater")
    else:
        print("c is the greater")

#biggest of 3 numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 >= n2 and n1 >= n3:
    print("n1 is big")
elif n2 >= n3:
    print("n2 is big")
else:
    print("n3 is big")

    
