1.#Even or odd
x=int(input("Enter the value: "))
if(x%2==0):
    print("Even")
else:
    print("odd")

#2.Variable swap
a=56
b=76
c=92
a,b,c=c,a,b
print(a,b,c)

#3.string reverse
s="hello world"[::-1]
print(s)

#4.list to string
x=list("School")
print(x)

#5.temperature convertor
c=int(input("enter the celius"))
f=(c*9/5)*32
print(f)

#6.data type checker
a=(35)
print(type(a))
b=(10.3)
print(type(b))
c=("college")
print(type(c))
d=["file"]
print(type(d))

#7.string reversal
K="villupuram"[::-1]
print(K)

#8.string concatentation
a="school"
b="college"
c=a,b
print(c)

#9.tyoe casting challenge
a="100"
b="25"
c='10.5'
a=int(a)
b=int(b)
c=float(c)
sum=a+b
sub=sum-c
output=str(sub)+"is the answer"
print(output)

#10.palindrome
n="123"
res=n[::-1]
if(res==n):
    print("palindrome")
else:
    print("not palindrome")  



#CHECKING 