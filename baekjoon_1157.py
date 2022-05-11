word = input().upper()
used_alpahbet = list(set(word))
cnt_list = []

for alphabet in used_alpahbet:
    cnt_list.append(word.count(alphabet))

max_num = max(cnt_list)
if cnt_list.count(max_num) > 1:
    print('?')
else:
    print(used_alpahbet[cnt_list.index(max_num)])