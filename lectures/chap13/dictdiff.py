import string,time

def process_file(filename):
    hist = dict()
    fp = open(filename, encoding='utf8')
    for line in fp:
        process_line(line, hist)
    return hist

def strip_punctuation(word):
    letters = []
    for letter in word:
        if letter.lower() in string.ascii_letters:
            letters.append(letter)
    return ''.join(letters)

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = strip_punctuation(word)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('thesunalsorises.txt')
words = process_file('words.txt')


def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

emma_words = subtract(hist, words)

print('Found', len(emma_words), 'not in list')
count = 128
for word in emma_words.keys():
    count -= 1
    print(word, end=' ')
    if count < 1:
        break

def subtract_lists(t1, t2):
    res = list()
    for item in t1:
        if item not in t2:
            res.append(item)
    return res

print('\n=========================\n')
now = time.time()
emma_dict = subtract(hist, words)
print('Dictionaries took:', time.time() - now)

hist_words = list(hist.keys())
words_words = list(words.keys())

now = time.time()
new_emma_words = subtract_lists(hist_words, words_words)
print('Lists took:', time.time() - now)

print('List method found:', len(new_emma_words))
