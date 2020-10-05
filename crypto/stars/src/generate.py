#!/usr/bin/env python3

import multiprocessing
import sys
from Crypto.Util.number import getPrime, isPrime


NUM_THREADS = 8


def worker(needed_count, minimal_diameter):
    while True:
        p = getPrime(1024)
        primes = [p]

        q = p + 2

        count = 1
        # print('...')

        while True:
            if isPrime(q):
                primes.append(q)
                count += 1

                if q - p > minimal_diameter.value:
                    # already worse than before
                    break

                if count == needed_count:
                    if q - p < minimal_diameter.value:
                        minimal_diameter.value = q - p
                        print('New minimal diameter =', minimal_diameter.value)
                        print(primes)
                        n = 1
                        for p in primes:
                            n *= p
                        print('n =', n)
                        print()
                    break

            q += 2


if __name__ == '__main__':
    needed_count = int(sys.argv[1])
    minimal_diameter = multiprocessing.Value('i', int(sys.argv[2]))

    for i in range(NUM_THREADS):
        multiprocessing.Process(target=worker, args=(needed_count, minimal_diameter)).start()
