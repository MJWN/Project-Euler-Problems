
def max_prime(n):
    i = 2
    while i * i <= n:
        if n%i == 0:
            n = n / i
        else:
            i = i + 1
    return n

print(max_prime(600851475143))