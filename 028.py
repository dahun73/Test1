seq1 = "ATGTTATAG"
li = []
for i in seq1:
    if i == 'A':
        li.append('T')
    elif i == 'T':
        li.append('A')
    elif i == 'C':
        li.append('G')
    elif i == 'G':
        li.append('C')
print(li)
print(''.join(li))



compseq = ""
compDic = {"A":"T", "C":"G", "G":"C", "T":"A"}
for s in seq1:
    compseq += compDic[s]

print(compseq)
