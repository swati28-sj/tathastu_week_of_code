n=int(input('Enter a number:'))
def odd_even(n):
    print(n,'is even number') if n%2==0 else print(n,'is a odd number')
        
def prime(n):
    flag1=1
    for i in range(2,n-1):
        if(n%i==0):
            flag1=0
    print(n,'is a prime number') if(flag1==1) else print(n,'is not a prime number')

def palindrome(n):
    t=str(n)
    r=t[::-1]
    print(n,'is a palindrome number') if(t==r) else print(n,'is not a palindrome number')

def armstrong(n):
    t=str(n)
    sum_int=0
    length=len(t)
    for i in t:
        sum_int+=int(i)**length
    print(n,'is a armstrong number')if(n==sum_int) else print(n,'is not a armstrong number')
odd_even(n)
prime(n)
palindrome(n)
armstrong(n)
