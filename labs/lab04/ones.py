import random

def generate_test(fname, n):
    fin = open(fname, 'w')
    for i in range(n):
        fin.write('0' * random.randint(1,10))
        fin.write('1' * random.randint(1,10))
        fin.write('0' * random.randint(1,10))
    fin.close()

# Global variables
in_ones = False
ones_count = 0

def initialize():
    global ones_count, in_ones
    in_ones = False
    ones_count = 0

def begin_ones(c):
    global in_ones
    return not in_ones and c == '1'

def end_ones(c):
    global in_ones
    return in_ones and c != '1'

def process_file(fname):
    global in_ones, ones_count
    initialize()
    fin = open(fname)
    for line in fin:
        for c in line:
            if begin_ones(c):
                in_ones = True
            elif end_ones(c):
                in_ones = False
                ones_count += 1
    return(ones_count)


fname = 'randomdigits.txt'

#random test cases
for i in range(10,21):
    n = random.randint(0,10000)
    generate_test(fname, n)
    print("Should be", n, end=': ')
    print(process_file(fname))

# special test cases
for n in (0,1,2,1000000):
    generate_test(fname, n)
    print("Should be", n, end=': ')
    print(process_file(fname))


