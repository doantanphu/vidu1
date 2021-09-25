x = lambda a:a + 10
y = lambda a, b: a + b

print(x(20))
print(y(100, 200))

def ham_mu(n):
    x = lambda x:x **n
    return x

tinhmu = ham_mu(3)
y= tinhmu(10)
print(y)

tinhmu = ham_mu(2)
print(tinhmu(5))
print(tinhmu(10))