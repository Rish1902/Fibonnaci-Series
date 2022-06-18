a=int(input("enter the limit"))
f=0
s=1
if a<=0:
    print("the limit is null",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        z=f+s
        print(z,end=" ")
        f=s
        s=z
