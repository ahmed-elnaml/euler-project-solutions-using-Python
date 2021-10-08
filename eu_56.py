# euler 56
def eu_56(n:int):
    sum=0
    num=n
    while num>9:
        sum=sum+(num%10)
        num=num//10
    else:
        sum=sum+(num%10)
    return sum
def f1(x):
    return 1+1/(1+x)

