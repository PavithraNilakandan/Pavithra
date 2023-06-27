##a=int(input("Enter the value of a:"))
##b=int(input("Enter the value of b:"))
##c=input("Enter a mathematical operator:")
##if(a!=0)and(b!=0):
##    if(c=="+"):
##        print("add=",a+b)
##    elif(c=="-"):
##        print("sub=",a-b)
##    elif(c=="*"):
##        print("product=",a*b)
##    elif(c=="/"):
##        print("division=",a/b)
##    elif(c=="%"):
##        print("modulus=",a%b)
##    elif(c=="//"):
##        print("floor division=",a//b)
##    elif(c=="**"):
##        print("exponential=",a**b)
##    else:
##        print("Enter correct operator")
##else:
##        print("Enter a valid number")


##leap year
##year=int(input("Enter the year:"))
##if(year%4==0):
##    if(year%100==0):
##        if(year%400==0):
##            print("It is a leap year")
##        else:
##            print("It is not a leap year")
##    else:
##            print("It is a leap year")
##else:
##  print("It is not a leap year")


####wage
##age=int(input("Enter the age:"))
##sex=str(input("Enter the sex(M,F):"))
##days=int(input("Enter the number of days worked:"))
##if(age!=0 and days!=0):
##    if(age>=18 and age<30 and sex=="M"):
##        print("wage=",700*days)
##    elif(age>=18 and age<30 and sex=="F"):
##                print("wage=",750*days)
##    elif(age>=30 and age<=40 and sex=="M"):
##                print("wage=",800*days)
##    elif(age>=30 and age<=40 and sex=="F"):
##                print("wage=",850*days)
##    else:
##                print("Enter appropriate gender")
##else:
##    print("Enter the correct age")



####library charge
##days=int(input("Enter the number of days:"))
##if(days!=0):
##    if(days>0 and days<=5):
##        amount=2*days
##        print("The charge is rs.",amount)
##    elif(days>=6 and days<=10):
##        amount=3*days
##        print("The charge is rs.",amount)
##    elif(days>=11 and days<=15):
##        amount=4*days
##        print("The charge is rs.",amount)
##    elif(days>15):
##        amount=5*days
##        print("The charge is rs.",amount)
##    else:
##        print("Enter the correct day number")
##else:
##    print("Number of days cannot be zero")



####kilometre
##km=int(input("Enter the kilometre covered:"))
##if(km!=0):
##    if(km<=10):
##        amount=11*km
##        print("The amount is:",amount)
##    elif(km>10 and km<=100):
##        amount=110+(km-10)*10
##        print("The amount is:",amount)
##    elif(km>100):
##        amount=1010+(km-100)*9
##        print("The amount is:",amount)
##else:
##    print("Enter the correct value")


####marks
##m1=int(input("Enter the marks scored in English:"))
##m2=int(input("Enter the marks scored in Math:"))
##m3=int(input("Enter the marks scored in Science:"))
##m4=int(input("Enter the marks scored in Social studies:"))
##if(m1>35 and m2>35 and m3>35 and m4>35):
##    if(m1>80 and m2>80 and m3>80 and m4>80):
##        print("Science stream")
##    elif(m1>80 and m2>50 and m3>50):
##        print("Commerce stream")
##    elif(m1>80 and m4>80):
##        print("Humanities")
##    else:
##        print("Enter the exactly scored marks")
##else:
##    print("You have failed")

      

######bonus
##salary=int(input("Enter the salary:"))
##service=int(input("Enter the years of service:"))
##if(service!=0):
##    if(service>10):
##        bonus=(10/100)*salary
##        print("Your bonus is:",bonus)
##    elif(service>=6 and service<=10):
##        bonus=(8/100)*salary
##        print("Your bonus is:",bonus)
##    elif(service<6):
##        bonus=(5/100)*salary
##        print("Your bonus is:",bonus)
##    else:
##        print("Enter the correct amount of salary")
##else:
##    print("Service cannot be zero")


####city
##city=str(input("Enter the city:"))
##if(city=="Delhi"):
##    print("The monument is Red Fort")
##elif(city=="Agra" or city=="Jaipur"):
##    print("The monument is Taj Mahal")
##else:
##    print("Enter the correct city")


####three digit number
##number=int(input("Enter the number:"))
##if(number!=0):
##    if(number>99 and number<1000):
##        print("The number is a three digit number")
##    else:
##        print("The number is not a three digit number")
##else:
##    print("Zero is invalid")


####greatest and lowest of two numbers
##a=int(input("Enter the value of a:"))
##b=int(input("Enter the valu of b:"))
##if(a>b):
##    print("a is greater")
##else:
##    print("b is greater")


####divisible by 2 and 3
##a=int(input("Enter the number:"))
##if(a%2==0 and a%3==0):
##    print("a is divisible by both 2 and 3")
##else:
##    print("a is not divisible by both 2 and 3")



##youngest and eldest
a=int(input("Enter the age of a:"))
b=int(input("Enter the age of b:"))
c=int(input("Enter the age of c:"))
d=int(input("Enter the age of d:"))
if(a>b and a>c and a>d):
    print("a is eldest")
elif(a<b and a<c and a<d):
    print("a is youngest")
elif(b>a and b>c and b>d):
    print("b is eldest")
elif(b<a and b<c and b<d):
    print("b is youngest")
elif(c>a and c>b and c>d):
    print("c is eldest")
elif(c<a and c<b and c<d):
    print("c is youngest")
elif(d>a and d>b and d>c):
    print("d  is eldest")
else:
    print("d is youngest")
