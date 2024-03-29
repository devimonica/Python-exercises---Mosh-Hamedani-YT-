# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

# Solution:

def prime_num(limit):
    prime_list = []
    for number in range(2, 100):
        prime = True
        for i in range(2, number):
            if number%i == 0:
                prime = False
        if prime == True:
            prime_list.append(number)
    print(prime_list)


prime_num(5)

# Solution:

def prime_num(limit):
    prime_list = []
    for number in range(2, limit):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_list.append(number)
    print(prime_list)


prime_num(25)
