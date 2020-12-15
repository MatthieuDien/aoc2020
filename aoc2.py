from itertools import product

l = []

c = 0

with open("input-2","r") as f:
    for line in f:
        range, char, word = line.split(' ')
        min, max = tuple(map(int, range.split('-')))
        char = char[0]
        # wc = word.count(char)
        # if min <= wc and wc <= max:
        #     c += 1
        if (word[min-1] == char) ^ (word[max-1] == char):
            c+=1
    print(c)
