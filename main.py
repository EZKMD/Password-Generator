import random as r

def passwordGenerator(length):
    uppercaseArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercaseArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbolsArray = ['[', ']', '@', '/', '\\', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '-', '_', '#', '\'', '<', '.', '>', ',', ':', ';', '=', '+' '~', '?', ' ']
    numbersArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  

    masterArray = [uppercaseArray, lowercaseArray, symbolsArray, numbersArray]
    password = []

    for i in range(0, length):
        x = r.randint(0,3)
        chosenArray = masterArray[x]
        y=r.randint(0,(len(chosenArray)-1))
        chosenCharacter = chosenArray[y]
        password.append(chosenCharacter)
    
    password = ''.join(password)

    return password


def main():
    length = int(input("Enter required length of password: "))
    password = passwordGenerator(length)
    print(password)

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram Terminated by User")
        break  
