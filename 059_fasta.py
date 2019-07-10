seq = ""
with open("059.fasta",'r') as fr:
    for line in fr:
        if line.startswith(">"):
            pass

        else:
            seq += line.strip()

print(len(seq))
    
    
    
    
    
    
    
    #    for line in fr:
#        li = fr.readlines()
#li.("\t")        
#li = ''.join(li)
#print(li)


