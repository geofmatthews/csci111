def sequence(n):
    print('Collatz sequence: ', end='')
    while n != 1:
        print(n, end=', ')
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n*3 + 1
    print(n)

sequence(3)
sequence(512)
sequence(513)
