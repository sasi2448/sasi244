c=int(input())
a=input()
b=a.split()
b.sort()
b.sort(key=len)
for i in b:
    print(i,end=' ')
