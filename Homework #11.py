numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    d = 0
    for k in range(2, i+1):
        if i % k == 0:
            d = d + 1
        if d == 1:
            is_prime = True
        else:
            is_prime = False
    if i == 1:
        continue
    elif is_prime == 1:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)