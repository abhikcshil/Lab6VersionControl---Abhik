"""
Lab 6: Version Control
Author: Abhik Shil
Class: COP3502C
Section: 22282
Description: Learning version control through git
"""

def encode(password):
    enc_password = "" #empty output string initiated
    if len(password) != 8: #ensures password is 8 characters long
        print("password was not 8 characters long")
        exit()

    encoding_dict = {0:3, 1:4, 2:5, 3:6, 4:7, 5:8, 6:9, 7:0, 8:1, 9:2}
    encoded_list = [encoding_dict[int(i)] for i in password] #adds 3 to each integer in password
    for i in encoded_list: enc_password += str(i) #combines all elements in encoded_list
    print("Your encoded password is:", enc_password)
    
def decode(user_input):
    password = ''
    
    for i in user_input:
        temp = str(int(i) - 3) 
        password += temp
        #user_input.replace(user_input[i], int(user_input[i]) += 3)
    print(password)

def main():

    user_input = input("Would you like to encode or decode your password? (enter: E/D)")
    if user_input == "E":
        password = list(input("Input an 8 digit password containing only integers")) #user inputs
        encode(password) #runs encode function on password
    if user_input == "D":
        password = input()
        decode(password)


if __name__ == "__main__":
    main()