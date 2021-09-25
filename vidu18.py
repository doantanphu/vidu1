def ham_mu(n):
    x = lambda x:x **n
    return x

tinhmu = ham_mu(3)
y= tinhmu(10)
print(y)

tinhmu = ham_mu(2)
print(tinhmu(5))
print(tinhmu(10))