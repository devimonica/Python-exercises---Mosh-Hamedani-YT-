# Write a function that returns the maximum of two numbers.

#print(max(4, 9)

def max_num(num1, num2):
    maximum_num = 0
    if num1 > num2:
        maximum_num = num1
    else:
        maximum_num = num2
    return maximum_num


print(max_num(4, 9))
