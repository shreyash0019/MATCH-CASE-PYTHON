s="""*********************************************************************
			Area of Different Figures
*********************************************************************
			R. Rectangle
			S. Square
			C. Circle
    		T. Triangle
			E. Exit
*********************************************************************"""
print(s)
ch=input("Enter Ur Choice:")
match(ch.upper()):
    case "R":
        print("Enter Length and Breadth")
        L,B=float(input()),float(input())
        print("Area of Rect={}".format(L*B))
    case "S":
        s=float(input("Enter Side:"))
        print("Area of Square={}".format(s**2))
    case "C":
        r = float(input("Enter Radius:"))
        print("Area of Circle={}".format(3.14*r ** 2))
    case "T":
        B,H=float(input("Enter Base of Triangle:")),float(input("Enter Hight of Triangle:"))
        print("Area of Triangle={}".format(1/2*B*H))
        print("------------OR---------------------")
        print("Enter Three Side of Triangle")
        a,b,c=float(input()),float(input()),float(input())
        s=(a+b+c)/2
        ta=(s*(s-a)*(s-b)*(s-c))**0.5
        print("Area of Triangle={}".format(ta))
    case "E":
        print("Thx for using this Program")
    case _:
        print("Ur Selection of Operation is wrong--try again")

