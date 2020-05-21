import sys


def sieve(primes, factor):
    for p in primes:
        if p != 0 and p != factor:
            if p % factor == 0:
                primes[primes.index(p)] = 0
    return primes


def main(argv):
    if len(argv) != 2:
        raise ValueError('Please enter exactly one argument, an integer limit'
                         ' to the size of the primes generated.')
    n = int(argv[1])
    if n < 2:
        raise ValueError('The integer limit must be greater than or equal to'
                         ' two.')
    primes = [i for i in range(2, n + 1)]
    for p in primes:
        if p != 0:
            primes = sieve(primes, p)
    print('\n'.join([str(p) for p in primes if p != 0]))


if __name__ == '__main__':
    main(sys.argv)
