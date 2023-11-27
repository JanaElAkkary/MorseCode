# morse code encrypter and decrypter.
print("welcome to Morse Translater")
print ("Enter text to encrypt using Morse code: ")

def morse_encrypter(message):
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
    message_after_encryption = " ".join(morse_dict_1.get(character,'') for character in message.upper()) 
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
    if message== "":
        print("Not Defined, Please Enter text to decrypt using Morse code: ")
    return message_after_decryption 

def morse_encrypter_arabic(message):
    message_after_encryption_arabic = " "
    morse_dict_3 ={'ا': '.-', 'ب': '-...', 'ث': '-.-.', 'د': '-..', 'ء': '.', 'ف': '..-.', 'غ': '--.', 'ح': '....',
    'ي': '..', 'ج': '.---', 
    'ك': '-.-', 'ل': '.-..', 'م': '--', 'ن': '-.', 'خ': '---',
    'ق': '--.-', 'ر': '.-.', 'س': '...', 'ت': '-', 'ط': '..-', 'ض': '...-', 'و': '.--', 'ص': '-..-',
    'ظ': '-.--', 'ذ': '--..','ز':'---.','ش':'----','ع':'.-.-','ه':'..-..'}
    message_after_encryption = " ".join(morse_dict_3.get(character,'') for character in message.upper()) 
    if message == "":
        print("Not Defined, Please Enter text to encrypt using Morse code:  ")
    return message_after_encryption_arabic










while True:
    choice = input("Choose 0 for exit, 1 for morse_encrypter, 2 for morse_decrypter, 3 for morse_ encrypter_arabic: ")
    if choice == '0':
        break
    elif choice == '1':
        message = input("Enter messege to encrypt: ")
        print(morse_encrypter(message))
    elif choice == '2': 
        message = input("Enter messege to decrypt: ")
        print(morse_decryptor(message)) 
    elif choice == '3':
        message = input("Enter message to encrypt from arabic: ")  
        print(morse_encrypter_arabic(message))                       
    else: 
       print("Undifined input") 
