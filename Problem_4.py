
def palindrome_check(number):
    number_solved = 0
    str_num = str(number)
    num_list = list(str_num)
    reverse_num_list = num_list[::-1]
    if num_list == reverse_num_list:
        number_solved = int(''.join(num_list))
    return number_solved


def largest_palindrome():
    check = 0
    range_1 = range(100,1000)
    range_2 = range(100,1000)
    
    for i in range_1:
        for r in range_2:
            num = i*r
            if num == 12221:
                print()
            palindrome_num = palindrome_check(num)
            if palindrome_num > check:
                check = palindrome_num
    return check

print(largest_palindrome())

   



