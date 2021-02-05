num1 = int(input("Input First Number: "))
num2 = int(input("Input Second Number: "))
num3 = int(input("Input Third Number:"))

if num1 < num2 and num2 < num3:
    print("Increasing order")
elif num1> num2 and num2> num3:
    print("Decreasing order")
else:
    print("Neither increasing or decreasing")
