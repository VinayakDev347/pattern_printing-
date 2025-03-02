# buy a number 
n = int(input("Enter the rows: "))
#-----------------------------1--------------------------------------
"""
*
**
***
****
*****

# code
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")

"""
#-----------------------------2--------------------------------------
"""
*****
****
***
**
*

#code
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")

"""
#-----------------------------3--------------------------------------
"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *

#code
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
"""
#-----------------------------4--------------------------------------
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * *

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print("")
"""