li = [3,1,1,2,0,0,2,3,3]
d1 = {} #key : number , value :frequency
d1[0] = int(li.count(0))
d1[1] = int(li.count(1))
d1[2] = int(li.count(2))
d1[3] = int(li.count(3))
print(d1)




l = "ACGTGAAGACTGACAATG"
d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


print(d)

for k,v in d.items():
    print(k,v)
