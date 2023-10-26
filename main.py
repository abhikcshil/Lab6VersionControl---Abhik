"""
Lab 6: Version Control
Author: Abhik Shil
Class: COP3502C
Section: 22282
Description: Learning version control through git
"""

def encode(password):
    enc_password = ""
    if len(password) != 8:
        print("password was not 8 characters long")
        exit()

    encoded_list = [int(i) + 3 for i in password]
    for i in encoded_list: enc_password += str(i)
    print("your encoded password is:", enc_password)

def main():

    password = list(input("Input an 8 digit password containing only integers"))
    encode(password)


if __name__ == "__main__":
    main()