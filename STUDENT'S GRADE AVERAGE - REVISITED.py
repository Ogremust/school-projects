name = str(input("Enter Name: "))
math = int(float(input("Enter Math: ")))
science = int(float(input("Enter Science: ")))
english = int(float(input("Enter English: ")))

f_math = 0
f_sci = 0
f_eng = 0

average = (math + science + english) / 3
print("Average Grade: ", "%.2f" % average)

if average >= 75:
    print("Congratulations!")
    print("You passed the semester")
    if math < 75:
        f_math = 1
    if science < 75:
        f_sci = 1
    if english < 75:
        f_eng = 1
    if (f_math or f_sci or f_eng) == 1:
        print("but you need to retake the following subject(s):")
        if math < 75:
            print("Math")
        if science < 75:
            print("Science")
        if english < 75:
            print("English")
else:
    print("You failed the semester")
