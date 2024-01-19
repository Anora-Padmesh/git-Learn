"""a={1:"a",2:3}
b={"name":3,"hi":9}
c=a.update(b)
print(c)
"""

#To add two dictionary
"""dict1={    "name":"janu",    "age":21,}
dict2={    "word":"deepu",    "num":21,}
for x in (dict2):
    dict1[x]=dict2[x]
print(dict1)"""

# using two list to make dictionary
"""a=["hi","this","ok"]
b=[1,2,3]
d={}
for k in a:
    for v in b:
        d[k]=v
        b.remove(v)
        break
print(d)
"""

"""a={"a":100, "b":200, "c":300}
c=0
for v in a.values():
    c=v+c
print(c)"""


"""a=int(input())
d={}
for i in range(a):
    k=input()
    v=input()
    d.update({k:v})
print(d)
"""
"""
a=int(input())
d=[]
for i in range(a):
    b=(input())
    d.append(b)
    print(d)
"""

"""d=20
c=[]

for i in range(1,d*d+1):
    if d==len(c):
        break
    elif i==1:
        c.append(i)
        continue
    elif i%2==0:
        pass
    elif i%7==0 and i//7<d or i%3==0 and i//3<d or i%5==0 and i//5<d:
        c.append(i)
print(c)
print(str(c)[-3:-1])"""



"""a={    "name":"janu",    "age":21,}
c=a.copy()
a["name"]="saran"
print(a)
print(c)"""




"""
def ascii(a):
    d={}
    t=[]
    for i in range(0,255):
        d[chr(i)]=i
    for i in a:
        for k,v in d.items():
            if i==k:
                t.append(v)
    return t

s=input("Enter the character to convert ascii : ")
print(ascii(s))"""

"""def comma(x,y):
    c=""
    for i in range(len(x)):
        c=c+y+x[i]
    d=c[1:]
    return('"'+d+'"')
n=int(input("Enter the size of the tuple: "))
d=[]
for i in range(n):
    a = input("enter the string ")
    d.append(a)
u=tuple(d)
b=input("enter the special character: ")
print(comma(u,b))
"""


"""def sort():
    for i in range(len(a)):
        t=0
        for k in range(i+1,len(a)):
            if a[i]>a[k]:
                t=a[i]
                a[i]=a[k]
                a[k]=t
    return a
def start_end():
    s=0
    e=len(a)-1
    while s<=e:
        m=(s+e)//2
        if a[m]==b:
            return m
        elif a[m]<b:
            s=m+1
        elif a[m]>b:
            e=m-1
    else:

        if m%2==0:
            return m
        else:
            return m-1
a=[1,2,5,9,12]

b=10

print(sort())
print(start_end())
"""

"""a=[5000,500,55,1,10]
b=900
for i in range(len(a)):
    t=0
    for k in range(i+1,len(a)):
        if a[i]>a[k]:
            t=a[i]
            a[i]=a[k]
            a[k]=t
print(a)
s=0
e=len(a)-1
while s<=e:
    m=(s+e)//2
    if a[m]==b:
        print("Element is found in index",m)
        break
    elif a[m]<b:
        s=m+1
    elif a[m]>b:
        e=m-1
else:
    z=a.copy()
    c=0
    d=[]
    for i in range(len(z)):
        c=abs(a[i]-b)
        d.append(c)
    y = 0
    f = d[0]
    for i in range(1,len(d)):
        if f>d[i]:
            f=d[i]
            y=i
    print("element is not found and near index is",y)
"""



"""p=(input("Enter the user name : "))
r=(input("Enter the user Role : "))
with open("prg10.csv","r") as f:
    d={}
    c={}
    l=[]
    for i in f:
        i=i.replace("\n", "").replace('"',"").split(",")
        l.append(i)
for i in l:
        c=len(i)
        d.update({i[0]:i[1:c+1]})
if p in d.keys():
    if r in d[p]:
        print(True)
    else:
        print(False)
else:
    print(False)
"""


"""a=["padmesh anora","fsdf fdasasd"]
b=[]
c={}
for i in a:
    i=i.split()
    b.append(i)
for i in b:
    for j in range(len(i)):
        c.update({i[0]:i[1]})
        continue

print(c)"""



"""from functools import reduce

def add(x, y):
    return x + y

list = [2, 4, 7, 3]
x=reduce(add, list)
print(x)
"""

"""def add(x):
    if x>2:
        return True

li = [2, 4, 7, 3]
x=filter(add, li)
for i in x:
    print(i)"""


"""a=[1,2,3,4]

y=list(filter(lambda x:x>3,a))
print(y)"""

"""from functools import reduce
def fun(x,y):
    c=[]
    if x<0:
        pass
    elif y<0:
        pass
    c.append((x,y))




a=[1,-2,-4]
x=reduce(fun,a)
print(x)
"""





"""a="abbcccaaaaa"
d=0
f=[]
for k in a:
    if d==len(a):
        break
    c = 0
    for i in range(d,len(a)):
        if a[d]==a[i]:
            c=c+1
        else:
            break
    d=d+c
    print(c)
    f.append(c)
print(f)"""
"""z=0
for i in range(len(f)):
    if (i+1)==f[i]:
        z=z+1
if z==len(f):
    print(True)
else:
    print(False)
"""
a=[1,2,3,4,5]
b=[2,3,4]
e=[]
for i in a:
    if i in b:
        e.append(i)
print(e)
