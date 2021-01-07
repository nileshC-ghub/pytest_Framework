
#Factorial Function by 123456

def factorial(n): 
    return 1 if (n<=1) else n * factorial(n - 1)

#Reverse Function by 123456

def reverse(n):
    rev = 0
    while n > 0:
        rem = n % 10  
        rev = (rev*10) + rem
        n = n//10  
    return rev
