import string

abc = string.ascii_lowercase
zyx = abc[::-1]

# Any of the following work:
def atbashlower(letter):
    letter = letter.lower() # no effect if not upper
    if letter.islower():
        return chr(ord('a') + ord('z') - ord(letter))
    else:
        return letter

def atbashlower(letter):
    letter = letter.lower() # no effect if not upper
    if letter.islower():
        return zyx[abc.index(letter)]
    else:
        return letter

def atbashlower(letter):
    letter = letter.lower() # no effect if not upper
    if letter.islower():
        for a,z in zip(abc, zyx):
            if letter == a:
                return z
    else:
        return letter

#Using one of the above:
def atbash1(letter):
    newletter = atbashlower(letter)
    if letter.isupper():
        newletter = newletter.upper()
    return newletter

def atbash(s):
    result = ''
    for letter in s:
        result = result + atbash1(letter)
    return result
