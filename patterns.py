# buy a number 
# n = int(input("Enter the rows: "))

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

# code
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

# code
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
# code
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print("")
"""
#-----------------------------5--------------------------------------

"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *

for i in range(n):
    for j in range(n - i - 1):
        print(" ",end=" ")
    for j in range(2 * i + 1):
        print("*",end=" ")
    print("")

#another method

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print("")
"""
#-----------------------------6--------------------------------------
"""
 * * * * * 
  * * * * 
   * * * 
    * * 
     *

n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print("")
"""
#-----------------------------7--------------------------------------

"""
*****
****
***
**
*

n = 5 
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")
"""
#-----------------------------8--------------------------------------
""" 
 *****
  ****
   ***
    **
     *

n = 5
for i in range(n, 0, -1):
    for j in range(0, n-i+1):
        print(" ",end='')
    for k in range(0, i):
        print("*", end='')

    print("")

    
"""
#-----------------------------9--------------------------------------
"""
n=5

* * * * * 
*       * 
*       * 
*       * 
* * * * * 

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j==0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
#-----------------------------10--------------------------------------
"""

*
**
***
****
*****
*****
****
***
**
*

n = 5
for i in range (1, n+1):
    for j in range (i):
        print("*", end="")
    print("")

for i in range (n,0,-1):
    for j in range (i):
        print("*", end="")
    print("")
"""
#-----------------------------11--------------------------------------
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()"
"""
