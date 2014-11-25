#!/usr/bin/python3
'''找出質數 '''
import math

def prepare_factor(max):
    prime = [1] * max
    for i in range(2, int(math.sqrt(max))):
        if prime[i] == 1:
            for j in range(2 * i, max):
                if j % i == 0:
                    prime[j] = 0
    #primes = [i for i in range(2, max) if prime[i] == 1]
    return  [i for i in range(2, max) if prime[i] == 1]

print(prepare_factor(1000000))
