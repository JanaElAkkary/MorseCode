import unittest 
import morsetranslator1
class TestMorseCode(unittest.TestCase):

    def test_encryption_all_uppercase(self):
        text = jana
        expected_output= 
        self.assertEqual(morsetranslator1.morse_encryptor(text),expected_output)

    def test_encryption_all_lowercase(self):
        self.assertEqual(morsetranslator1.morse_encryptor("hello world"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_with_numbers(self):
        self.assertEqual(morsetranslator1.morse_encryptor("H3ll0 W0r1d"),".... ...-- .-.. .-.. ----- / .-- ----- .-. .---- -..")

    def test_encryption_Characters_alphabet_numbers(self):
        self.assertEqual(morsetranslator1.morse_encryptor("H3ll0-W0r1d!!!"),".... ...-- .-.. .-.. ----- -....- .-- ----- .-. .---- -.. -.-.-- -.-.-- -.-.--")
    
    def test_encryption_with_numbers_characters(self):
        self.assertEqual(morsetranslator1.morse_encryptor("2023@1234--"),"..--- ----- ..--- ...-- .--.-. .---- ..--- ...-- ....- -....- -....-")

    def test_decryption_without_space(self):
        self.assertEqual(morsetranslator1.morse_decryptor(".... .."), "HI")
    
    def test_decryption_with_spaces(self):
        self.assertEqual(morsetranslator1.morse_decryptor(".... .. / -- -.-- / -. .- -- . / .. ... / ... .... .- .... -.."), "HI MY NAME IS SHAHD")
    
    def test_decryption_numbers_characters(self):
        self.assertEqual(morsetranslator1.morse_decryptor(".---- ..--- ...-- -....- ..--.. ..--.."),'123-??')
    

        


if __name__ == '__main__':
    unittest.main()
