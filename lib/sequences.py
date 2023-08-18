#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return []
    elif length==1:
        print([0])
        return [0]
    elif length==2:
        print([0,1])
        return [0,1]
    fibonacci_sequence = [0, 1]
    for i in range(2,length):
        next_num=fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    print(fibonacci_sequence)
    return fibonacci_sequence       
print_fibonacci(9)    