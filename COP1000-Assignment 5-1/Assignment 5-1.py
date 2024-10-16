#this will be Assignment 5-1 Determine the Output of the PsuedoCode
#Declarations of all variables
a=1
b=2
c=5
d=4
e=6
f=7
g=4
h=6
j=2
k=5
n=9
p=2
q=4


#Example A
while a < c:
    a=a+1
    b=b+c
print("A=" + str(a))
print("B=" + str(b))
print("C=" + str(c))

#Example B (Shouldnt change because 4<7)
while d > f:
    d=d + 1
    e = e - 1
print("D=" + str(d))
print("E=" + str(e))
print("F=" + str(f))

#Example C
while g < h:
    g= g + 1
print("G=" + str(g))
print("H=" + str(h))

#Example D
while j < k:
    m = 6
    while m < n:
        print("Goodbye")
        m = m + 1
    j=j+1

#Example E
j=2
k=5
m=6
n=9
while j < k:
    while m < n:
        print("Hello")
        m = m +1
    j=j + 1

#Example F
while p < q:
    print("Adios")
    r=1
    while r < q:
        print("Adios")
        r= r+1
    p = p + 1
