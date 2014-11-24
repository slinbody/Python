#!/usr/bin/python3
""" GCD practice """
def gcd(m,n):
    m ,n = n , m % n
    if n == 0 :
        return m
    else :
        return gcd(m,n)
a,b = input("Input:").split()

print(gcd(int(a),int(b)))
