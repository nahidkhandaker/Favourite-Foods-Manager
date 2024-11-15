# this project done by Nahid Khandaker

favourite_foods = [] #initialize empty list for favourite foods

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View favourite all foods")

    choice = input("Choose an option ") #From taken user input

    if choice == "0":
        print("Thanks for using Favourite Foods Manager ")
        break
    elif choice == "1":
        food = input("Enter your favourite food ") #Ask user for favourite food
        favourite_foods.append(food) #Add favourite food to list
        print("Food added successfully ")
    elif choice == "2":
        food = input("Enter the food you want to remove ") #Ask user for food to remove    
        if food in favourite_foods:
            favourite_foods.remove(food) #Remove food from list
            print(f"{food} remove successfully ")
        else: 
            print(f"{food} food doesn't exist in the list ")

    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods are: ")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}. {food}")
        else:
            print("No favourite foods yet ")

    else:
        print("Invalid choice. Please choose a valid option ") #If user enters invalid choice, print
