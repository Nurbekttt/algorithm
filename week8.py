def function(a,low,high):
    mid=(high+low)//2
    print(mid,"mid")
    if mid not in a:
        return mid
    else:
        lower=[]
        bigger=[]

        for i in a:
            print(i)
            if mid>i:
                lower.append(i)
            elif mid<i:
                bigger.append(i)
        print(bigger)
        if len(a)%2==0:
            if len(lower)>len(bigger):
                return function(bigger,mid-1,high)
            else:
                return function(lower,low,mid-1)
        else:
            print (len(lower),len(bigger))
            if len(lower)==len(bigger):
                return function(bigger,mid-1,high)
            else:
                return function(lower,low,mid-1)
#print(function([1,7,6,4,5,3],1,7))
def task1(a):
    c=0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                c+=1
    print c
#task1([4,1,3,2])
def zhelayak(a):
    l=[0]
    for i in range(len(a)):
        if l[-1]+40<a[i]:
            l.append(a[i])
    print(l)
#zhelayak([20,50,100])
def SMM(F,M,S):
    d=dict()
    people=0
    for i in range(len(F)):
        d[F[i]]=M[i]
    sort=dict()
    index=0
    print(d)

    for k in sorted(d):
        sort[k]=d[k]
        index+=1
    print(sort)
    for k in sort:
        print(k)
        print(people,"p")
        if S-sort[k]*k>0:
            people+=sort[k]
            S-=sort[k]*k
        else:
           people+=S//k
           break
    return people
#print(SMM([150,100],[1000,1500],150600))
def task2average(arr):
    summa=0
    for i in arr:
        summa+=i
    return summa/len(arr)
import copy
def task8(P,D):
    d=[]
    for i in range(len(P)):
        d.append(P[i]/D[i])
    print d
    z=copy.copy(d)
    d.sort()
    print(z)
    print(d)
    arr=[]
    for i in range(len(d)):
        for j in range(len(z)):
            if z[i]==d[j]:
                arr.append(len(z)-1-j)
    return arr

#print task8([100000,20000,40000],[5,3,1])
#def q12(a,s):

def q9(m,n):
    l=[0,0]
    for i in range(1,n):
        if not n%i:
            l.append(i)
    print l
    summ=0
    for i in range(len(l)):
        summ+=l[i]
        print summ
        if summ-m>0:
            for j in range(i+1):
                for k in range(i+1):
                    if summ-l[j]-l[k]==m and j!=k:
                        z=l[:i+1]
                        z.remove(l[k])
                        z.remove(l[j])
                        print("Z",z,l[k],l[j])
                    elif l[j]+l[k]==m and j!=k:
                        print (l[j],l[k],"Z")
        elif summ-m==0:
            print("Y")

q9(23,25)








