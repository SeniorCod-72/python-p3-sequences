#!/usr/bin/env python3

def print_fibonacci(length):
    print_fibonacci = len([0])
    print(print_fibonacci)
    pass
def print_fibonacci(n):
    if n == 0:
        print("[]")
        return
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence[:n])
