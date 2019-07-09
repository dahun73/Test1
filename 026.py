seq1 = "AGTTTATAG"
#print((seq1[0:3]) + (seq1[3:6]) + (seq1[-3:]))


for i in range(0, len(seq1), 3):
    print(i, seq1[i:i+3])
