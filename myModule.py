def calcGC(s):
    num_c = s.count("C")
    num_g = s.count("G")
    gc = float(num_c + num_g)/len(s) * 100
    return gc

if __name__ == "__main__":   #이 부분을 쓰는 이유는 import할 때 실행되지 않도록 하기위함. 밖에서 파이썬을 실행할 때만 실행되도록 한다!!!
    s = ""
    with open("sequence.txt", 'r') as fr:
        for line in fr:
            s += line.strip()

    print(s)

    gc = calcGC(s)
    print(gc)
