import sys
from math import sqrt; from itertools import count, islice
import numpy as np

primes = np.load('primes.npy')
file_name = sys.argv[1]

def is_prime(n: int) -> bool:
#    if n < 15485867:
     return n in primes
#    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

with open(file_name) as input_numbers:
    for line in input_numbers:
        number = int(line)
        print(1 if is_prime(number) else 0)

