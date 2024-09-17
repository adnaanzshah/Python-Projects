fruits = []
j=int(input("Enter the number of fruits : "))

for i in range(j):
    fruit = input(f"Enter the name of fruit {i+1} : ")
    fruits.append(fruit)

for fruit in fruits:
    print(fruit)