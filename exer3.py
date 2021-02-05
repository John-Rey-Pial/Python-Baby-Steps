num1 = int(input("Input First Number: "))
num2 = int(input("Input Second Number: "))
num3 = int(input("Input Third Number: "))

if num1!= num2 and num2!= num3  and num3 != num1:
    print("All numbers are different")
elif num1 == num2 and num2 == num3 and num3 == num1:
    print("All numbers are equal")
elif num1 == num2 or num2 == num3 or num1 != num2 or num2!= num3:
    print("Neither all are equal nor different")