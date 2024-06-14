d={}
s="hey there, i love python"
for i in s:
    d[i]= d.get(i,0) + 1
    print(d)
    print(i)