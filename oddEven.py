# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

number = input("Please enter a number")
number = int(number)

if (number % 2):
    print("Your number is odd ")
else:
    print("Your number is even ")