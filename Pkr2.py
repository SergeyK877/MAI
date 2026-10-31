
def inf():
    a = 1
    while True:
        yield a
        a =a +1

g =inf()
for i in range(10):
    print(next(g))