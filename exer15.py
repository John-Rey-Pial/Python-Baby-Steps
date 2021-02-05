cars = []
prices = []


invalid = False
while invalid != True:
    user_input = int(input("1. Add Car\n2. View Cars\n3.  Quit\n:"))
    if (user_input  == 1):
        cars.append(input("Car name: "))
        prices.append(input("Price: "))
    elif (user_input == 2):
        print("Cars and Prices:")
        for x in range (0, len(cars)):
            print(f"{cars[x]}- {prices[x]}")
    elif (user_input ==3):
        invalid =True
    else:
        print("Invalid Input. Try Again")