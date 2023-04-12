'''arr = [1,2,3,4,1,2,3,4,5,7]
s= '55dd55'
def one(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i] +=1
    for i in dic.keys():
        if dic[i]==1:
            print(i,end=" ")
    print()
one(arr)
def evens(arr):
    even = 0
    odd = 0
    for i in arr:
        if i&1==0:
            even +=1
        else:
            odd +=1
    print(even,end=" ")
    print(odd)
evens(arr)
def add(s):
    a =0
    temp =''
    for i in s:
        if i.isalpha():
            if len(temp) != 0:
                a +=int(temp)
        else:
            temp +=i
    print(a)
add(s)
lis = [1,2,0,3,0,5,0]
def xero(lis):
    temp =[]
    count = 0
    for i in lis:
        if i==0:
            count +=1
        else:
            temp.append(i)
    for i in range(count):
        temp.append(0)
    print(temp)
xero(lis)
def cxero(lis):
    ls_0=-1
    count =0
    for i in range(len(lis)):
        if lis[i] ==0 and count==0:
            ls_0 = i
            count +=1
        elif lis[i] !=0 and count !=0:
            lis[i],lis[ls_0] = lis[ls_0],lis[i]
            ls_0+=1
    print(lis)
cxero(lis)
def prime(num):
    i=2
    while i*i<num:
        if num%i==0:
            print('no')
        else:
            continue
    print('prime')
prime(int(input("enter the number for prime")))
def factorial(num):
    if num==0 or num ==1:
        return 1
    return num * factorial(num-1)
print(factorial(int(input("enter the number for fatorial"))))
def lcm(a,b):
    gret=max(a, b)
    for i in range(gret,(a*b)+1):
        if i%a==0 and i%b==0:
            print(i)
            break
    else:
        print(a*b)
lcm(int(input('enter a: ')), int(input('enter b: ')))
def gcd(a,b):
    if b==0:
        print(a)
    else:
        gcd(b, a%b)
gcd(int(input("enter a for gcd: ")),int(input('enter b for gcd: ')))
def fun(n):
    if n>10:
        return
    print(n,end=' ')
    return fun(n+1)
fun(1)
print()
def fun1(n):
    if n==0:
        return 
    print(n,end=' ')
    fun1(n-1)
fun1(10)
def funb(n):
    if n>10:
         return
    funb(n+1)
    print(n)
funb(1)
def rev(a,s,e):
    if s>e:
        return a
    a[s],a[e]=a[e],a[s]
    return rev(a, s+1, e-1)
print(rev([2,3,4,5],0,3))'''
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(4))
def eodi(n):
    even = 0
    odd = 0
    while n>0:
        d = n%10
        if d&1==0:
            even +=1
        else:
            odd +=1
        n //=10
    return even,odd
print(eodi(2001))
def rev(n):
    num = n
    r = 0
    while n>0:
        d = n%10
        r = (r*10)+d
        n //=10
    if r==num:
        return "yes"
    return "no"
print(rev(101))