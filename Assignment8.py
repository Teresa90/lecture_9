#Write a program that inputs 5 numbers from the user in a loop and finds the sum of the numbers.

#program prompts the user to input five numbers
get_number=[int(input("Enter integer #%d: "%(i)))
# we implement our for loop
   for i in range(1,6)]

print("Numbers:",get_number,"\nSum:",sum(get_number),"\nAverage:",sum(get_number)/5)

