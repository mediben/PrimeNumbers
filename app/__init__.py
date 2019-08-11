from views import get_primes

if __name__ == "__main__":
    a = 1200
    if isinstance(a, (int, long)) :
        res = get_primes(a+1)
        print(res)
    else:
        print('Please provide integer number')
