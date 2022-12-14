years = int(input("Enter years in service: "))
office = str(input("Enter office: "))

if office == "IT":
    if years >= 10:
        print("Amount given: 10000")
    else:
        print("Amount given: 5000")

if office == "ACCT":
    if years >= 10:
        print("Amount given: 12000")
    else:
        print("Amount given: 6000")

if office == "HR":
    if years >= 10:
        print("Amount given: 15000")
    else:
        print("Amount given: 7500")
