
# a = input()
# d = {}
# for c in a:
#     if c in d:d[c]+=1
#     else: d[c]=1
    
# print(d)

import ast
a = ast.literal_eval(input())
def rm(a):
    if isinstance(a,list)==1:
        h = [rm(x) for x in a if x]
        return h
    elif isinstance(a,dict)==1:
        rs={}
        for k in a:
            v = a[k]
            if k and v: rs[k]=rm(v)
        return rs
    elif isinstance(a,set)==1:
        g ={rm(x) for x in a if x}
        return g
    return a
print(rm(a))


import time

def timer(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        r = f(*args, **kwargs)
        t2 = time.time()
        print("Время выполнения:", t2 - t1)
        return r
    return wrapper

@timer
def sum_numbers(n):
    s = 0
    for i in range(n):
        s = s + i
    return s

print(sum_numbers(1000000))


def infinite():
    a = 1
    while True:
        yield a
        a = a + 1

g = infinite()
for i in range(10):
    print(next(g))






