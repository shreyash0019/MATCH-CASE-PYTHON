#MatchCaseEx1.py
print("*"*50)
print('Temprature Conversion Calculator')
print("*"*50)
print("\t1. F to C")
print("\t2. F to K")
print("\t3. C to F")
print("\t4. C to K")
print("\t5. K to F")
print("\t6. K to C")
print("\t7. Exit")
print("*"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        F=float(input("Enter the Temp in terms of F:"))
        C = (F - 32)*(5 / 9)
        print("\tGiven Temp in terms of F:{}".format(F))
        print("\tEQV . Temp in terms of C:{}".format(C))
    case 2:
        F = float(input("Enter the Temp in terms of F:"))
        K = (F - 32)*(5 / 9) + 273.15
        print("\tGiven Temp in terms of F:{}".format(F))
        print("\tEQV . Temp in terms of K:{}".format(K))
    case 3:
        C = float(input("Enter the Temp in terms of C:"))
        F = C*(9 / 5) + 32
        print("\tGiven Temp in terms of C:{}".format(C))
        print("\tEQV . Temp in terms of F:{}".format(F))
    case 4:
        C = float(input("Enter the Temp in terms of C:"))
        K = C + 273.15
        print("\tGiven Temp in terms of C:{}".format(C))
        print("\tEQV . Temp in terms of K:{}".format(K))
    case 5:
        K = float(input("Enter the Temp in terms of K:"))
        C = K - 273.15
        print("\tGiven Temp in terms of K:{}".format(K))
        print("\tEQV . Temp in terms of C:{}".format(C))
    case 6:
        K = float(input("Enter the Temp in terms of K:"))
        F = (K-273.15)*(9/5) + 32
        print("\tGiven Temp in terms of K:{}".format(K))
        print("\tEQV . Temp in terms of C:{}".format(F))
    case 7:
        print("Thx for Using this program")
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Program execution completed")