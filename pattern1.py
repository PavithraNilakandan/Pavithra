##* * * * *
##* * * *
##* * *
##* *
##*

size=int(input("enter the rows value"))
for i in range(size,0,-1):
    for j in range(i,0,-1):
       print("*",end=" ")
    print()
for i in range(1,size+1):
    for j in range(0,i+1 ):
        print("*",end=" ")
    print()


##size=4
##i=size=4
##i=4->0 T
##    j=4 4->0 T
##        *
##    j=3 3->0 T
##        * *
##    J=2 2->0 T
##        * * *
##    J=1 1->0 T
##        * * * *
##    J=0 0->0 F
##i=3 3->0 T
##    j=3 3->0 T
##        * * * *
##        *
##    j=2 2->0 T
##        * * * *
##        * *
##    j=1 1->0 T
##        * * * *
##        * * *
##    j=0 0->0 F
##i=2 2->0 T
##    j=2 2->0 T
##        * * * *
##        * * *
##        *
##    j=1 1->0 T
##        * * * *
##        * * *
##        * *
##    j=0 0->0 F
##i=1 1->0 T
##    j=1 1->0 T
##        * * * *
##        * * *
##        * *
##        *
##    j=0 0->0 F
####i=0 0->0 F
##
##

##
##row=int(input("enter the rows value:"))
##for i in range(1,row+1,1):
##    for j in range(1,i+1,1):
##       print("*",end=" ")
##    print()
##
##
##/rows=int(input("enter the rows value:"))
####for i in range(1,rows+1,1):
####    for j in range(1,row+1,1):
##        if(j>=i):
##            print("*",end=" ")
##        else:
##            print(" ")
##      print()




rows=int(input("enter value of row:"))
for i in range(0,rows,1):
    for j in range(0,i,1):
        print(" ",end=" ")
    for k in range(rows,i,-1):
        print("*",end=" ")
    print()
        
               


































