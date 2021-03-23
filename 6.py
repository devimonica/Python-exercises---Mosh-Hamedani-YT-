# Write a function called show_stars(rows). If rows is 5, it should print the following:

#     *
#     **
#     ***
#     ****
#     *****

# Solution:

def show_stars(rows):
    for number in range(1, rows+1):
        print('*'*number)


show_stars(5)
