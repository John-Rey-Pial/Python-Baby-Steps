num1= int(input("Input First Number: "))
num2= int(input("Input Second Number: "))
num3= int(input("Input Third Number: "))

if num1>=num2 and num1>=num3:
        print(f"The greatest:{num1}")
elif num2>=num3 and num2>=num1:
        print(f"The greatest: {num2}")
else:
    print(f"The greatest: {num3}")