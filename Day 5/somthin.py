# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(x, y):
        return x
    return pair(first)

def cdr(pair):
    def second(x, y):
        return y
    return pair(second)

print(car(cons(1, 2)))
print(cdr(cons(1, 2)))


