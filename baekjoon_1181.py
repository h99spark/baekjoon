n = int(input())
words = [input() for i in range(n)]

words = list(set(words))
len_words_list = list()
for word in words:
    len_words_list.append([len(word), word])

len_words_list.sort(key = lambda x: (x[0], x[1]))

for length, word in len_words_list:
    print(word)