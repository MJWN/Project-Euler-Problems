def gen(a, b, max):
    while a < max:
        yield a
        a, b = b, a + b
        


def fibonacci(a, b, end):
    count = 0
    for item in gen(a, b, end):
        if item % 2 == 0:
            count += item

    return count


print (fibonacci(1, 2, 4000000))

