import random
i = 1
ds = {}
while (i<=10):
    a =  random.randint(1,10)
    ds.update({str(i) : a})
    i += 1
print(ds)