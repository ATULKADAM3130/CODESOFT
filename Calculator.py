#Task:1 = Calculator
while(True):
    print("1.Additon")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Mode(%)")
    print("6.Power of Number")
    print("7.floor_Divison")
    print("8.Exit")

    choise=int(input("Enter the choise :"))

    if(choise==1):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Addition=Num1+Num2
        print("Addition of Num1 & Num2 is :",Addition)

    elif(choise==2):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Substraction=Num1-Num2
        print("Substraction of Num1 and Num2 is :",Substraction)

    elif(choise==3):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Multiplication=Num1*Num2
        print("Multiplication of Num1 & Num2 is :",Multiplication)
    
    elif(choise==4):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Division=Num1/Num2
        print("Division of Num1 & Num2 is :",Division)

    elif(choise==5):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Mode=Num1 % Num2
        print("Mode of Num1 & Num2 is :",Mode)

    elif(choise==6):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Power=Num1**Num2
        print("Power of Num1 & Num2 is :",Power)

    elif(choise==7):
        Num1=int(input("Enter the number 1 :"))
        Num2=int(input("Enter the number 2 :"))
        Floor_Divison=Num1 // Num2
        print("Floor Diviion of Num1 & Num2 is :",Floor_Divison)

    elif(choise==8):
        break

    else:
     print("Invalid Choise taken")