num = 5
result = 1

while num > 0:
    result *= num
    num -= 1
print(result)


def fact(n):
    if n == 1:
        return 1 #마지막에 탈출
    else:
        return n * fact(n-1)   #재귀함수 특징

result = fact(5)
print(result)

#fact(5) -> else에서 fact(4) fact(3) fact(2) fact(1) 돌고 if n=1가서 1 반환


#피보나치 수열
#f(n) + f(n+1) = f(n+2)
