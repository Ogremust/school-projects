name = str(input("Enter your name: "))
math = int(float(input("Enter your grade in Math: ")))
science = int(float(input("Enter your grade in Science: ")))
english = int(float(input("Enter your grade in English: ")))

average = (math + science + english) / 3

print("Your average is: ", "%.2f" % average)

if average >= 75:
    print("Congratulations!")
    print("You passed the semester")
else:
    print("You failed the semester")
