#Modify the previous program so that it prints square root instead of square.
#Use the function in the math module. Update the print message accordingly

from math import sqrt   #absolute importing
def main():
    num = int(input("Enter a number:"))
    result = (sqrt(num))
    print("The square root of ",num,"is",result)
    
main()
