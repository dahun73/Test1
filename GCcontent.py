with open("sequence.txt", 'r') as fr:
    for line in fr:
        line = line.strip().split('\t')
        print(''.join(line))

