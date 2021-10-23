#let there is given alphabet and key

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#CAESAR AND NUMBER THEORY FUNCTIONS
#basic modular function 
def modulo(a,b):
    rem = a % b
    print ()
    print ("The modulo of %d of %d is %d" % (a,b,rem))
    print ()
#    return rem

#caesar encrypt code algorithm
def caesar_encrypt(plain_text, KEY):
    
    #The encrypted message
    cipher_text = ''
    
    #make small letter case to upper case
    plain_text = plain_text.upper()
    
    #consider all the letters in the plain text
    for c in plain_text:
        index = ALPHABET.find(c)
        #caesar encryption is simple shift
        #need to divide and get modulo by length of caesar encryption
        index = (index+KEY)%len(ALPHABET)
        #keeping encrypt word
        cipher_text = cipher_text + ALPHABET[index]
        
    return cipher_text

#caesar decrypt code algorithm
def caesar_decrypt(cipher_text, KEY):
    
    #The decrypted message
    plain_text = ''
    
    #consider all the letters in the plain text
    for c in cipher_text:
        index = ALPHABET.find(c)
        #caesar encryption is simple shift
        #need to divide and get modulo by length of caesar encryption
        index = (index-KEY)%len(ALPHABET)
        #keeping decrypt word
        plain_text = plain_text + ALPHABET[index]
        
    return plain_text

def caesar_crack(cipher_text):
    
    #get all element size of the Alphabet
    
    cipher_text = cipher_text.upper()
    for KEY in range(len(ALPHABET)):
        
        #reinitiallize this to be empty
        plain_text = ''
        
        #Caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index-KEY)%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
            
        print("with key %s, the result is %s"%(KEY,plain_text))

#GENERAL FUNCTIONS
def user_friendly():
    print()
    WORD = input("Type encrypt: ")
    KEY = input("Type your key: ")
    KEY = int(KEY)
    print()
    return WORD, KEY

def user_word():
    print()
    WORD = input("Type encrypt: ")
    print()
    return WORD

def terminate():
    print ()
    print("TERMINATING the MENU")
    print ()

