#PROBLEM 1

##INTRODUCTION

###exercise 1: "Say "Hello, World!" With Python":
stringa = 'Hello, World!'
print(stringa)


###exercise 2: "Python If-Else":
n=int(input())
if n%2!= 0:
    print("Weird")
elif n>=2 and n<=5:
    print("Not Weird")
elif n>=6 and n<=20:
    print("Weird")
else:
    print("Not Weird")


###exercise 3: "Arithmetics Operators":
a = int(input())
b = int(input())
    
print(a+b)
print(a-b)
print(a*b)


###exercise 4: "Python: Division":
a = int(input())
b = int(input())

print(a//b)
print(a/b)


###exercise 5: "Loops":
n = int(input())

for i in range(0,n):
    print (i**2)


###exercise 6: "Write a function":
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))


###exercise 7: "Print Function":
n = int(input())

for i in range(1,n+1):
    print(i, end='')







