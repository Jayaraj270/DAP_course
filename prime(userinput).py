#program 1:Write a Python program that takes a number from the user and checks whether it is prime or not?
number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
