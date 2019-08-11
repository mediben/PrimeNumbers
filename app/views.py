
def get_primes(n):
    # Based on Eratosthenes Sieve
    # Initially all numbers are prime until proven otherwise
    # False = Prime number, True = Compose number
    nonprimes = n * [False]
    count = 0
    nonprimes[0] = nonprimes[1] = True
    prime_numbers = []
    for i in range(2, n):
        if not nonprimes[i]:
            prime_numbers.append(i)
            count += 1
            for j in range(2*i, n, i):
                nonprimes[j] = True
    return prime_numbers
