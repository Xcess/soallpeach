import sys
from math import sqrt; from itertools import count, islice
import numpy as np
import itertools




primes = np.load('prime_small.npy')
file_name = sys.argv[1]

@profile
def is_devidable(item):
    # if item < 10006:
    #     return not item in primes
    if item < 99460729:
        array = primes
    else:
        array = itertools.chain(primes, islice(count(10007, 2), int((sqrt(item)+1)/2)))
    for i in array:
        if item%i == 0:
            return True
    return False





f = open(file_name, 'r')
input_numbers = f.readlines()

maxnum = 1
for line in input_numbers:
    if int(line) > maxnum:
        maxnum = int(line)



f.seek(0)
for line in input_numbers:
    number = int(line)
    print(1 if not is_devidable(number) else 0)

