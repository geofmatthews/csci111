

def common_factor(a,b):
    for n in range(2, min(a,b)+1):
        if a%n == 0 and b%n == 0:
            return True
    return False

def can_be_added(ls, n):
    return n not in ls and common_factor(n, ls[-1])

def extend_sequence(ls):
    n = 1
    while not can_be_added(ls, n):
        n += 1
    ls.append(n)

def ecg_seq_index(n):
    if n < 3:
        return n - 1
    ls = [1,2]
    while n != ls[-1]:
        extend_sequence(ls)   
    return len(ls)-1

def ecg_seq_element(n):
    if n < 2:
        return n+1
    ls = [1,2]
    for i in range(n-1):
        extend_sequence(ls)
    return ls[-1]

if __name__ == '__main__':
    for i in range(10):
        print(i, ecg_seq_element(i), ecg_seq_index(i))
    




    
