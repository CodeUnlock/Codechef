s=input()
g=input()
count=0
if(len(s)>10):
    for i in s:
        if(i==g):
            count+=1
print(count)