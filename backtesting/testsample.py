from itertools import islice

def window(seq, n=2):
    print('testts')
    it = iter(seq)
    result = tuple(islice(it, n))

    if len(result) == n:
        yield result

    for elem in it:
        result = result[1:] + (elem,)
        yield result

ss = [1,2,3, 6,7,8, 10,22,5, 3,64,33, 23,234,34, 234,7,11, 6,7,8, 34,35,8]

dd = window(ss, 2)
for row in dd:
    pass

def next_number():
    yield 0
    yield 1
    yield 2

for i in next_number():
    print(i)


sample = ["20210101", "20210102", "20210103", "20210104", "20210105", "20200106"]

it = iter(sample)
for i in it:
    print(i)