
def avoids(word, letters):
    return False

def uses_all(word, letters):
    return False

vowels = 'aeiou'

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if avoids(word, vowels):
        print(word)
