
a = input()
d = {}
for c in a:
    if c in d:d[c]+=1
    else: d[c]=1
    
print(d)