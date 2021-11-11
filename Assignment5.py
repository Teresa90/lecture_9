#Write the factorial program that we saw in the class in a new window,
#Save and Run
#This function computes the factorial
#of a number entered by the user

def factor():
    n=int(input("Please enter a whole number:"))
    fact = 1

    for factor in range(1, n+1):
        fact = fact * 5
        print("The factorial of", n, "is", fact)
factor()

