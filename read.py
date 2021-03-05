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


#新增一個功能 :
#哪一個字最常出現
wc = {} #word_count
for d in data:
    words = d.split()  #預設就是空白鍵，且會將連續空白都切掉
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  #新增一個key到字典，並賦值為1

for word in wc:
    if wc[word] > 1000000:
        print(word,wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input("請問你想查甚麼字?")
    if word == 'q':
        print("感謝使用本功能。")
        break
    if word in wc:
        print(word,"出現過的次數為:",wc[word])
    else:
        print('沒有出現過這個字。')
