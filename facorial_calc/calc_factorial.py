# Just a Demo Self Written Code for calculating factorial of any given number

num=10
# num=int(input("Enter a number : "))
fact=1
factorial=1
while(fact<num):
    factorial=fact*factorial
    fact=fact+1

print(f"{num}! = ",factorial)
