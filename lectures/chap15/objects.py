
class Thing:
    """ holds values """

def initialize(thing):
    thing.a = 1
    thing.b = 2
    thing.c = 3
    thing.d = 4

def process(thing):
    thing.a = 2*thing.a
    thing.b = 2*thing.b
    thing.c = 2*thing.c
    thing.d = 2*thing.d
    return thing

def printThing(thing):
    print('Thing:',thing.a, thing.b, thing.c, thing.d)

thing = Thing()
initialize(thing)
printThing(thing)
process(thing)
printThing(thing)
initialize(thing)
printThing(thing)
