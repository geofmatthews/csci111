#!/usr/bin/env python

import sys

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    print('The sum of %d and %d is %d'% (n1, n2, n1 + n2))
except:
    print('Usage: %s <n1> <n2>' % sys.argv[0])
    print('<n1> and <n2> must be integers')
    

