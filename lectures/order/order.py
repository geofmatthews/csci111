
names = ['geof', 'anne', 'bob', 'zelda', 'larry', 'susie']
nums =  [ 111  ,   222 ,  333,   444,     555,     666]

for tupe in (sorted(zip(names,nums))):
    print(tupe)

def order(ls):
    index = list(range(len(ls)))
    index.sort(key=lambda i : ls[i])
    return index

ord = order(names)
print(ord)

for i in ord:
    print(names[i], nums[i])
               
    
