

def encode(password):
    encodedPassword = ""
    for digit in password:
        encodedDigit = str((int(digit)+3)%10)
        encodedPassword += encodedDigit
    return encodedPassword

def decode(encodedPassword):
    decodedPassword = ""
    for digit in encodedPassword:
        decodedDigit = str((int(digit)-3)%10)
        decodedPassword += decodedDigit
    return decodedPassword

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Enter an option: ")

        if option == 1:
            password = input("Please enter your password to encode: ")
            encodedPassword = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is " + encodedPassword + ", and the original password is " + decode(encodedPassword))

        elif option == 3:
            break

if __name__ == "__main__":
    main()