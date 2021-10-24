import Caesars

if __name__ == '__main__':
    
    #Prints the 4 options 
    while True:
        print()
        print("CHOOSE THE MENU BELOW")
        print()
        print("1. Demonstrating modulo") #demonstrates how modulo function works
        print("2. Encrypt word and Decrypt back") #encrypts input and decryptes it back to original
        print("3. SOLVING Encrypt Word") #prints out the key 
        print("4. EXIT") #terminates program
        print()
        NUMBER = input("Type Number: ") #integer input

        if NUMBER == "1": #modulo option
            print()
            print("Type a for dividend and b for divisor")
            a = input("Type your a: ")
            a = int(a)
            b = input("Type your b: ")
            b = int(b)
            Caesars.modulo(a,b) #prints remainder
            
        elif NUMBER == "2": #encrypt and decrpyt option
            #Let the user type the word and key
            WORD, KEY = Caesars.user_friendly() #prompts user to input a string

            encrypted = Caesars.caesar_encrypt(WORD, KEY)
            print("encrypted word is ", encrypted) #prints encrypted string
            decrypted = Caesars.caesar_decrypt(encrypted, KEY)
            print("decrypted word is ", decrypted) #prints decrypted string

        elif NUMBER == "3": #determining key option
            #Let the user type the word
            WORD = Caesars.user_word() #prompts string input
            encrypted = WORD
            Caesars.caesar_crack(encrypted) #returns the key number

        else: #terminate program
            Caesars.terminate()
            break
