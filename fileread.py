

with open("test.txt",'r') as fr:
    for line in fr:
        print(line.strip())


fr.close()
