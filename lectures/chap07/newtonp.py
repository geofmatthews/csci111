def newtonp(n):
    x = 10
    while abs(x**2/n - 1) > 1e-3:
        x1 = round(x, 2)
        x2 = round(x**2, 2)
        x3 = round(n/x, 2)
        frac = (x + n/x)/2
        x4 = round(frac, 2)
        x5 = round(frac**2, 2)
        
        x = frac
    return x

x = newtonp(5)
print(x, x**2)

x = newtonp(5000)

print(x, x**2)

def newton(n):
    x = 10
    while abs(x**2/n - 1) > 1e-5:
        x = (x + n/x)/2
    return x

for i in range(5,10):
    print(i, newton(i), newton(i)**2)
