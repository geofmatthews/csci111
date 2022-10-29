def newton(n):
    x = 10
    while abs(x**2/n - 1) > 1e-5:
        x = (x + n/x)/2
    return x

for i in range(5,10):
    print(i, newton(i), newton(i)**2)
