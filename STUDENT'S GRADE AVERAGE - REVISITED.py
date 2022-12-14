name = str(input("Enter Name: "))
math = int(float(input("Enter Math: ")))
science = int(float(input("Enter Science: ")))
english = int(float(input("Enter English: ")))

average = (math + science + english) / 3
print("Average Grade: ", "%.2f" % average)
sub = {math, science, english}

if average >= 75:
    print("Congratulations!")
    print("You passed the semester")
    if (math or science or english) > 75:
        print("but you need to retake the following subject(s):")
        if math < 75:
            print("Math")
        if science < 75:
            print("Science")
        if english < 75:
            print("English")
    if not (math or science or english) > 75:
        print("but you need to retake the following subject(s):")
        if math < 75:
            print("Math")
        if science < 75:
            print("Science")
        if english < 75:
            print("English")
else:
    print("You failed the semester")
