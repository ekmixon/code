import itertools


@profile
def primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1


if __name__ == '__main__':
    n = 2000
    total = sum(itertools.islice(primes(), n))
    print('The sum of the first %d primes is %d' % (n, total))

