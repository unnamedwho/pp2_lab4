#ex - 1
"""
def gen_square(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input())
for i in gen_square(N):
    print(i)
"""
#ex - 2
"""
def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
for i in even(n):
    print(i)
"""
#ex - 3
"""
def check(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
check(n)
for i in check(n):
    print(i)
"""
#ex - 4
"""
def squares(a, b):
    for i in range(a, b):
        yield i ** 2

a = int(input())
b = int(input())
for i in squares(a, b):
    print(i, end=", " if i!=b and i != b - 1 else " " )

"""
#ex - 5
"""
def down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for i in down(n):
    print(i, end=", " if i != -1 else " ")
"""