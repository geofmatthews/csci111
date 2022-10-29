import string

histogram = dict()

def add_word(hist, word):
    if word not in hist:
        hist[word] = 1
    else:
        hist[word] += 1

fin = open('mobydick.txt', encoding='utf8')
for line in fin:
    if '*** START' in line:
        break
for line in fin:
    if '*** END' in line:
        break
    in_word = False
    word = ''
    for c in line:
        if c in string.ascii_letters:
            if not in_word:
                in_word = True
                word = c
            else:
                word += c
        if c not in string.ascii_letters:
            if in_word:
                add_word(histogram, word.lower())
                in_word = False

index = 0
print1 = False
print2 = False
def second(item):
    return item[1]
for key,value in sorted(histogram.items(),
                        key=second,
                        reverse=True):
    index += 1
    if 1 <= index <= 10:
        if not print1:
            print1 = True
            print('Top 10 words:')
        print(index, key, ':', value)
    if index > len(histogram) - 10:
        if not print2:
            print2 = True
            print('Bottom 10 words:')
        print(index, key, ':', value)
print('Special words:')
for word in ['moby', 'dick', 'ishmael', 'ahab', 'obsessed',
             'death', 'dead', 'god', 'devil',
             'heaven', 'hell']:
    if word in histogram:
        print(word, ':', histogram[word])
    else:
        print(word)
        
        
        
    
