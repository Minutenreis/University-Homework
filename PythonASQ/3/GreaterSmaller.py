n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if n1 > n2:
    if n1 % 10 == 0:
        print("The first number is greater and divisible by 10.")
    else:
        print("The first number is greater.")
elif n1 < n2:
    if(n2 % 2 == 0):
        print("The second number is greater and even.")
    else:
        print("The second number is greater and uneven.")
else:
    print("The numbers are equal.")