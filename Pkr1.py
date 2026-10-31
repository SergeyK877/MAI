import time

def timer(f):
    def wrap(a, b):
        t1 = time.time()
        
        r = f(a, b)
        t2 = time.time()
        
        print("Время выполнения" ,t2- t1)
        return r
    return wrap

@timer
def S(a,b):
    s = a +b
    return s

print(S(10,15))