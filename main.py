#Elias Sandoval
#Partner: Brian Santillan
def printMenu(): #function for print menu. This will display the option for the user.
    while True:
        print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit\n")
        option = int(input("Please enter an option: "))
        if option in [1 ,2 ,3]:
            return option
        else:
            print("Invalid Input!\nPlease enter an integer value between 1 and 3")

def encodePassword(password): #Function for encode password.
    newPassword = ""
    for digit in password:
        newDigit = int(digit) + 3
        newPassword += str(newDigit)

    return newPassword

def decodePassword(password): #function to decode the password (made by Brian)
    newPassword = ""
    for digit in password:
        newDigit = int(digit) - 3
        newPassword += str(newDigit)

    return newPassword

def main(): # main function code
    while True:
        option = printMenu()
        if option == 1:
            password = input("Please enter your password to encode: ")
            encodedPassword = encodePassword(password)
            print("Your password has been encoded and stored!")
            print(encodedPassword)
        elif option == 2:
            decodedPassword = decodePassword(encodedPassword)
            print(f"The encoded password is {encodedPassword}, and the original passcode is {decodedPassword}.")
        elif option == 3:
            quit()

if __name__ == "__main__":
    main()