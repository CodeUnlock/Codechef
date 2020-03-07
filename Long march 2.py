num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];
def countSetBitsRec(num):
    nibble = 0;
    if (0 == num):
        return num_to_bits[0];
    nibble = num & 0xf;
    return num_to_bits[nibble] + countSetBitsRec(num >> 4);


for _ in range(int(input())):
    n, q = [int(x) for x in input().split()]
    a = list(map(int, input().split()))
    p = [];c=[]
    for i in range(q):
        p1=int(input())

        b = []
        e = 0
        o = 0
        for i in a:
            if(bin(i^p1).count('1')%2==0):
                e += 1

        c.append(e)
    for i in c:
        print(i,len(a)-i)




