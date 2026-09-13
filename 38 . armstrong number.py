# Program to check if a three-digit number is Armstrong

num = int(input("Enter a three-digit number: "))

sum = 0
y = num

while (y > 0):
    digit = y % 10             # extract last digit
    sum = sum + digit**3       # add cube of digit
    y = y // 10                # remove last digit

if (num == sum):
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")


    
num = int(input("Enter a three-digit number: "))

rev = 0
x = num

while (num > 0):
    digit = num % 10        # extract last digit
    rev = rev + digit**3   # build reverse number
    num = num // 10        # remove last digit

if (x == rev):
    print(x, "is a Palindrome")
else:
    print(x, "is NOT a Palindrome")
