grade = int(float(input("Enter average grade: ")))

if grade <= 100:
    if grade >= 95:
        print("Excellent")
    else:
        if grade >= 90:
            print("Outstanding")
        else:
            if grade >= 85:
                print("Very Good")
            else:
                if grade >= 80:
                    print("Good")
                else:
                    if grade >= 75:
                        print("Poor")
                    else:
                        if grade >= 0:
                            print("Failed")
                        else:
                            if grade < 0:
                                print("Grade out of range")
else:
    if grade > 100:
        print("Grade out of range")