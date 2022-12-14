num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

low = 0
high = 0

if num1 > num2 and num1 > num3:
    high = num1
elif num2 > num1 and num2 > num3:
    high = num2
elif num3 > num1 and num3 > num2:
    high = num3

if num1 < num2 and num1 < num3:
    low = num1
elif num2 < num1 and num2 < num3:
    low = num2
elif num3 < num1 and num3 < num2:
    low = num3

total = low + high

print("Lowest:", low)
print("Highest:", high)
print("Sum:", total)
