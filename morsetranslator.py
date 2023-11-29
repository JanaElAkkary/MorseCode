# morse code encrypter and decrypter.
print("welcome to Morse Translater")
print ("Enter text to encrypt using Morse code: ")
#this is just a wwelcome and an introduction.
def morse_encryptor(message):
    message_after_encryption = " "
    morse_dict_1 ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'}
     #defining the encryptor and writing the first dictionary.
    message_after_encryption = " ".join(morse_dict_1.get(character,'') for character in message.upper()) 
    #we added join here to join all the answer in the quotation marks.
    #next is the upper part where we add "upper " to change every thing to upper case before translating the code because the dictionary is all in uppercase.
    if message == "":
        print("Not Defined, Please Enter text to encrypt using Morse code:  ")
    return message_after_encryption

print("Enter text to decrypt using Morse code: ")
def morse_decryptor(message):
    message_after_decryption=" "
    morse_dict_2= {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
    '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '/': ' '}
    message_after_decryption="".join (morse_dict_2.get (character,'')for character in message.split())
    # here we added ".join" takes all elments and joins them into a string.
    # we used .split breaks down a bigger string into several smaller strings.
    if message== "":
        print("Not Defined, Please Enter text to decrypt using Morse code: ")
    return message_after_decryption 


while True:
    choice = input( "1 for morse_encrypter, 2 for morse_decrypter, or Choose 0 for exit: ")
    if choice == '0':
        break
    elif choice == '1':
        message = input("Enter messege to encrypt: ")
        print(morse_encryptor(message))
    elif choice == '2': 
        message = input("Enter messege to decrypt: ")
        print(morse_decryptor(message))                   
    else: 
       print("Undifined input") 

#using while loop is to keep the app going until it breaks using 0.