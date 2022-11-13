

def initialize(d):
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4

def process(d):
    for c in 'abcd':
        d[c] = 2*d[c]        

def printDict(d):
    for c in 'abcd':
        print(d[c], end=' ')
    print()

thing = dict()
initialize(thing)
printDict(thing)
process(thing)
printDict(thing)
initialize(thing)
printDict(thing)
