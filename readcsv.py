import myModule

with open("test.csv", 'r') as fr:
    headerlist = fr.readline().strip().split(",")
    for line in fr:
        l = line.strip().split(",")
        id_ = l[0]
        seq = l[1]
        species = l[2]
        if species == "Herpes":
            gc = myModule.calcGC(seq)
            print(gc)
