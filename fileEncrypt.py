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
    f = Fernet(key) #create a fernet object with the key in it
    token = f.encrypt(contents.encode()) #encrypts the contents of the file and saves to a variable
    print ('\nEncrypted contents: \n' + token.decode()) #this is the output of the encrypted text
    print ('\nEncryption key (keep this somewhere safe!) \n' + key.decode()) #prints the key for user to writr down

    print('\nName of output file: ')
    file2Name = input() #name of the file that will have encrypted data saved to it
    file2 = open(file2Name, 'w') #opens the output file in "write mode"
    file2.write(token.decode())  #writes encrypted data to the file

    print('\nOutput encryption key to .txt file (y/n)')
    keyToText = input()
    
    if keyToText == 'y': #key gets saved to a text file "key.txt"
        keyFile = open('key.txt', 'w') #open the key file in "write mode"
        keyFile.write(key.decode()) #writes the key to the file
        keyFile.close() #always close your files when done!
   
    file2.close()
    file.close()

    main() #return to main function

#this unction take a file of users choice along with a key and decrypts said
#file with the key, then outputs it in the console
def decryptFile():

    #enter the key to be used to decrypt the file
    print('Enter key: ')
    key = input()
    byteKey = key.encode() #typecasting. encryption keys need to be bytes to be used, user enters 
                           #it as a bunch of chars
   
    f = Fernet(byteKey) #create the fernet object with the key in byte form
   
    print('Enter file name:')
    fileName = input() #user chooses a file to decrypt
   
    #file is opened in "read mode" and it's contents are saved to variable
    file = open(fileName, 'r') 
    contents = file.read()
   
    decryptedContents = f.decrypt(contents.encode()) #decrypts the contents and saves it in variable
    print('\n File contents: \n' + decryptedContents.decode()+ '\n') #outputs the decrypted contents
   
    file.close() #always close these things!!!

    main()


#the main function of the code. kicks things off
def main():

    print('Do you want to encrypt or decrypt a file?')

    option = input() #triggers the encrypt, decrypt or exit commands
    
    if option == 'encrypt':
        encryptFile() #calls the encrypt function

    elif option == 'decrypt':
        decryptFile() #calls the decrypt function

    elif option == 'exit':
        exit() #exits the program

    #exception handling
    else:
        print("Incorrect input! Choose from encrypt, decrypt or exit.")
        main()


main()
