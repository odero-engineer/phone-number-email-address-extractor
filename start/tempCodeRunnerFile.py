
def collatz(number):
    if number % 2 == 0:
        newNum = number / 2
        print(newNum)
        return newNum
    else:
        newNum = 3 * number + 1
        print(newNum)
        return newNum

user_input = int(input("Enter an Integer: "))

while user_input != 1:
    user_input = collatz(user_input)
