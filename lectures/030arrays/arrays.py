
rows, cols = 3,4

def dict_init():
    return dict()
def dict_set(d, i, j, val):
    d[i,j] = val
def dict_get(d, i, j):
    return d[i,j]

def list_init(nrows = rows, ncols = cols):
    result = [None]*nrows
    for i in range(nrows):
        result[i] = [None]*ncols
    return result
def list_set(t, i, j, val):
    t[i][j] = val
def list_get(t, i, j):
    return t[i][j]

def fixed_init(nrows=rows, ncols=cols):
    return [None]*(nrows*ncols)
def fixed_set(f, i, j, val, ncols=cols):
    f[i*ncols + j] = val
def fixed_get(f, i, j, ncols=cols):
    return f[i*ncols + j]


array_dict = dict_init()
array_list = list_init()
array_fixed = fixed_init()

for i in range(rows):
    for j in range(cols):
        dict_set(array_dict, i, j, i*j)
        list_set(array_list, i, j, i*j)
        fixed_set(array_fixed, i, j, i*j)

for i in range(rows):
    print()
    for j in range(cols):
        print(dict_get(array_dict, i, j), end=":")
        print(list_get(array_list, i, j), end=":")
        print(fixed_get(array_fixed, i, j), end="   ")
        
    
