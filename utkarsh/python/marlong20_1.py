for _ in range(int(input())):
    n,m = [int(i) for i in input().split()]
    a = [int (i) for i in input().split()]
    b = [int (i) for i in input().split()]
    temp = []
    for i in range(1,m+1):
        sum = 0
        for j in range(n):
            if(j in a):
                if(i==a[j]):
                sum=sum+b[j]
            else:
                sum = 9999999
        if(sum!=0):
            temp.append(sum)
    print(min(temp))
