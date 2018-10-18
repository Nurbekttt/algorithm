'''def locating(a):
    for i in range(1,len(a)-1):
        if a[i-1]<a[i]>a[i+1]:
            return a[i]
    if(a[0]==a[-1]):
        return a[0]
    elif a[0]>a[-1]:
        return a[0]
    else:
        return a[-1]
#print(locating([10, 20, 15, 2, 23, 90, 67]))
def shifted(a):
    for i in range(len(a)-1):
        if (a[i]>a[i+1]):
            return a[i]
    return a[-1]
#print(shifted([35, 42, 5, 15, 27, 29]))'''
#############################################
def power(x,n):
    if n==0:
        return 1
    if (n%2 == 0):
        return power(x,n//2)*power(x,n//2)
    else:return power(x,n//2)*power(x,n//2)*x
#print(power(4,9))
#print(pow(4,9))
def locate(arr, low, high, n):
    mid = low + (high - low) // 2
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return locate(arr, low, (mid - 1), n)
    else:
        return locate(arr, (mid + 1), high, n)

array=[10, 20, 15, 2, 23, 90, 67]
n=len(array)
high=n-1
#print(locate(array, 0,high, n))
array1=[35, 42, 5, 15, 27, 29]
finish=len(array1)-1
start=0
def shift(a,start,finish):
    mid=start+(finish-start)//2
    if(start==finish):
        return a[start]
    if(a[mid]>a[start]):
        return shift(a,mid,finish)
    else:return shift(a,start,mid)

print(shift(array1,start,finish))
