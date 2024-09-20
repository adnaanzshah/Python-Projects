# Just a Demo Self Written Code for calculating factorial of any given number

# num=10
# num=int(input("Enter a number : "))
def factorial(num):
    fact=1
    factorial=1
    while(fact<(num+1)):
        factorial=fact*factorial
        fact=fact+1
        print(f"{num}! = ",factorial)
    return (f"{num}! = ",factorial)

factorial(4)

n=5
def factorial_recursion(n):
    if (n==1 or n==0):
        return 1
    return(n*factorial_recursion(n-1))
print(factorial_recursion(5))