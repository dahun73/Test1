seq1 = "ATGTTATAG"
#print(seq1.index('C'))

for s in seq1:
    b = (s == "C")
    print(s, b)
    if b:
        break


print("C" in seq1)
