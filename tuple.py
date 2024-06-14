t = (50,78,90)
print (t[0])
t[0] = 28
print (t, type (t))

l = list (t)
l[0] = 28
t = tuple (l)