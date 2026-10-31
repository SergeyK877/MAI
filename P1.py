
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









