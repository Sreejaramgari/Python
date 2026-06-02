n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
if n1 % 2 == 0:
    print("n1 is even")
else:
    print("n1 is odd")
if n2 % 2 == 0:
    print("n2 is even")
else:
    print("n2 is odd")
if n2 % 2 == 0:
    print("n3 is even")
else:
    print("n3 is odd")

##practice------------------------------------------------------
#print 1 to 10 using for and while 
#for
for i in range(1, 11):
    print(i)
#while
i = 1
while i <= 10:
    print(i)
    i += 1
#sum of natural numbers from 1 to 10  using for loop and while loop
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)
#while
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i += 1 
print(sum)
# Print Even Numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#while
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
#count vowels and consonants using the word python
s = "Python"
vowels = 0
consonants = 0
for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)
#loops------------------------------------------------------------
#for loop(fine which one is even or odd from list of numbers)
lst = [1, 2, 3, 4, 5]
for ind in range(0, 5, 1):
    if lst[ind] % 2 == 0:
        print(lst[ind], "is even")
    else:
        print(lst[ind], "is odd")
#print even numbers between 20 to 40 using for loop
for i in range(20,41,2):
    print(i)
#
for i in range(20, 41):
    if i % 2 == 0:
        print(i)
#print 1 - 100 numbers using for loop
for i in range(1,101,1):
    print(i)
#using end parameter
for i in range(1,101,1):
    print(i, end = " ")

#find the sum of n natural numbers
total = 0
for num in range(1, 7):
    total = total + num
    print(total)
#find the sum of n natural numbers approach 1
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total = total + i
print(total)

#while loops ---------------------------------------------------------Practice problems
#print 1 to 100 numbers
num = 1
while num < 101:
    print(num)
    num += 1 #output:display from 1 to 100
#
num = 1
while num < 101:
    num += 1
    print(num) # outout :display numbers from 2 to 101
#print even numbers between 10 to 40
num = 10
while num <= 40:
    print(num)
    num += 2
#print odd numbers between 1 to 50
num = 1
while num <= 50:
    print(num)
    num += 2
#find which one is even or odd from list of numbers
lst = [11, 12, 13, 14, 15]
ind = 0
while ind < len(lst):
    if lst[ind] % 2 == 0:
        print(lst[ind], "is even")
    else:
        print(lst[ind], "is odd")
    ind += 1

#find sum of even numbers upto n
n = int(input("Enter a number: "))
sum = 0 #for sum of numbers sum = 0,for multiplication sum = 1
i = 1 #initialize
while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i += 1
print("Sum of even numbers =", sum)
#
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 2
    print(sum)
#print the numbers from 100 t0 1
num = 100 
while num > 1:
    print(num)
    num -= 1
#find the sum of even numbers between the range 'n' and 'm' using for loop
n = int(input("Enter n: "))
m = int(input("Enter m: "))
total = 0
for i in range(n, m + 1):
    if i % 2 == 0:
        total += i
print(total)
        
#using while loop
n,m = map(int,input.split())
total = 0
while n < m:
    if n % 2 == 0:
        total += n
        n += 1
        print(total)
#
n,m = map(int,input.split())
total = 0
if n % 2 != 0:
    n = n + 1
    while n < m:
        if n % 2 == 0:
            total += n
            n += 1
            print(total)

#find the length of number
n = 156
count = 0
while n > 0:
    n //= 10
    count += 1
    print(count)
#sum of digits in a number
n = 156
sum = 0
while n > 0:
    rem = n % 10
    n //= 10
    sum += rem
    print(sum)
#reverse a num
n = 123
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10
    print(rev)
#check wheather the number is palindrome or not
n = 121
temp = n
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10
    print(rev)
    print(n)
    if temp == rev:
        print("Palindrome")
    else:
        print("Not palindrome")
# check wheather the number is armstrong or not
n = 153
temp = n
rev = 0
order = len(str(n))   # number of digits
while n > 0:
    rem = n % 10
    rev = rev + (rem ** order)
    n //= 10
    print(rev)
    print(n)
if temp == rev:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
#to check weather the number is perfect number or not
n = 6
temp = n
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum = sum + i
        print(sum)
        print(i)
    i += 1
if temp == sum:
    print("Perfect number")
else:
    print("Not a perfect number")
    


    

