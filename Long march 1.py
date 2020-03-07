for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d = dict()
    c=[]
    cost=0
    for i in a:
        cost=0
        for j in range(0,n):
            if(a[j]==i):
                cost=cost+b[j]
        d[i]=cost
    print(min(d.values()))



