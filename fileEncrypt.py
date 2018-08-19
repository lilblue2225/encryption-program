from passlib.hash import pbkdf2_sha256 as passlib
from cryptography.fernet import Fernet

#this function takes a file of your choice and encrypts it's contents then
#outputs it to a file, with the option of saving the key to a file as well.
def encryptFile():
    
    print ('Enter file name: ')
    fileName = input() #user enters name of file to be encrypted
    file = open(fileName, 'r') #file is opened in "read mode"
    contents = file.read() #contents of file is saved to variable for use

    key = Fernet.generate_key() #this generates an encryption key. DO NOT LOSE THIS AS IT'S 
                                #NEEDED TO DECRYPT THE FILE LATER
    f = Fernet(key)
    token = f.encrypt(contents.encode()) #encrypts the contents of the file and saves to a variable
    print ('\nEncrypted contents: \n' + token.decode()) #this is the output of the encrypted text
    print ('\nEncryption key (keep this somewhere safe!) \n' + key.decode()) #prints the key for user to writr down

    print('\nName of output file: ')
    file2Name = input() #name of the file that will have encrypted data saved to it
    file2 = open(file2Name, 'w') #opens the output file in "write mode"
    file2.write(token.decode())  #writes encrypted data to the file

    print('\nOutput encryption key to .txt file (y/n)')
    keyToText = input()
    
    if keyToText == 'y':
        keyFile = open('key', 'w')
        keyFile.write(key.decode())
        keyFile.close()
   
    file2.close()
    file.close()

    main()


def decryptFile():

    #declarations...
    fileName = ''
    key = ''
    decryptedContents = ''
    

    print('Enter key: ')
    key = input()
    byteKey = key.encode()
   
    f = Fernet(byteKey)
   
    print('Enter file name:')
    fileName = input()
   
    file = open(fileName, 'r')
    contents = file.read()
   
    decryptedContents = f.decrypt(contents.encode())
    print('\n File contents: \n' + decryptedContents.decode())
   
    file.close()

    main()


def main():

    print('Do you want to encrypt or decrypt a file?')

    option = input()
    
    if option == 'encrypt':
        encryptFile()

    elif option == 'decrypt':
        decryptFile()

    elif option == 'exit':
        exit()

    else:
        print("Incorrect input! Choose from encrypt, decrypt or exit.")
        main()


main()


"""
TODO:
-Program runs fine
-comment all the code
"""