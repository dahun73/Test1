fr = open('test.txt', 'r')
lines = fr.xreadlines()
for s in lines:
    print(s.strip())

fr.close()
