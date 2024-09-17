fruits = []
j = int(input("Enter number of Fruits: "))

for i in range(j):
    fruit = input(f"Enter the name of fruit : ")
    fruits.append(fruit)

print("All Fruits names stored.")

while True:
    choice = int(input("Choose:\n\t 1 to Push \n\t 2 to Pop \n\t 3 to exit "))
    match choice:
        case 1:
            num = int(input("Enter how many number of new fruits you would like to add: "))
            for _ in range(num):
                n_fruit = input("Enter the name of new fruit: ")
                fruits.append(n_fruit)
            opt = input("If you wish to see the list type 'n' , default is 'y' : ")
            if opt == 'n':
                print("\n")
            else:
                print(fruits)
                
        
        case 2:
            num = int(input("Enter how many number of fruits you would like to pop: "))
            for _ in range(num):
                print("Below is the list of fruits, remember the indexing next to the fruit you wish to pop.")
                for idx, fruit in enumerate(fruits, start=1):
                    print(f"{idx}. {fruit}")
                p = int(input("Enter the index of the fruit you wish to pop: ")) - 1
                if 0 <= p < len(fruits):
                    fruits.pop(p)
                else:
                    print("Invalid index.")
            opt = input("If you wish to see the list type 'y', else type 'n': ")
            if opt == 'y':
                print(fruits)
            else:
                print("\n")
        
        case 3:
            import sys
            sys.exit()
        
        case _:
            print("Invalid choice. Please try again.")
