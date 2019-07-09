seq1 = "AGTTTATAG"
#li = []
#for i in seq1:
#    li.append(i)
#li.reverse()
#print(li)
#print(''.join(li))



#-------------- 방법2:거꾸로 인덱싱하여 문자열 첨가
revseq1 = ""  
for i in range(len(seq1)-1, -1, -1):
    revseq1 += seq1[i]
print(revseq1)


print(seq1[::-1]) #아주 간단, 파이썬만 가능
