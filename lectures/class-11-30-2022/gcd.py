
import random, time

def gcd_slow(a,b):
    for i in range(min(a,b)+1, 1, -1):
        if a%i == b%i == 0:
            return i
    return 1

def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a

if __name__ == '__main__':
    n = 10_000_000
    for test in range(10):
        a = random.randint(n, 10*n)
        b = random.randint(n, 10*n)
        now = time.time()
        g = gcd(a,b)
        print('Fast: %s seconds' % (time.time() - now))
        now = time.time()
        gs = gcd_slow(a,b)
        print('Slow: %s seconds' % (time.time() - now))
        print('a: %s  b: %s    gcd: %s' % (a,b,g))
        assert(g == gs)
        assert(a%g == 0)
        assert(b%g == 0)
