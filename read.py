data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))

print('檔案讀取玩了，總共有',len(data),'筆資料。')

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言的平均長度為:',sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有',len(new),'筆留言長度小於100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有',len(good),'筆留言，有提到good這個字')

"""
list comprehension:
1.
    good = [d for d in data if 'good' in d]
    有提到good的留言，就加進good[]

2.
    bad = ['bad' in d for d in data]
    有提到bad的留言，印True，否則印False
"""