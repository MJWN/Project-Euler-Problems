
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.#
# Find the sum of all the multiples of 3 or 5 below 1000.

number_list = range(1,1000)

def sum_three_and_five(my_list):
    count = 0
    for item in my_list:
        if item % 3 == 0 or item % 5 == 0:
            count += item
    return count

print (sum_three_and_five(number_list))
