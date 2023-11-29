import unittest 
import morsetranslator1
class TestMorseCode(unittest.TestCase):

    def test_encryption_uppercase(self):
        text = "JANA"
        expected_output=".--- .- -. .-"
        self.assertEqual(morsetranslator1.morse_encryptor(text),expected_output)

    def test_encryption_lowercase(self):
        text = "jana"
        expected_output=".--- .- -. .-"
        self.assertEqual(morsetranslator1.morse_encryptor(text),expected_output)

    def test_encryption_with_numbers(self):
        text= "jana1910"
        expected_output=".--- .- -. .- .---- ----. .---- -----"
        self.assertEqual(morsetranslator1.morse_encryptor(text),expected_output)

    def test_encryption_Characters_alphabet_numbers(self):
        text="jana@1910"
        expected_output = ".--- .- -. .- .--.-. .---- ----. .---- -----"
        self.assertEqual(morsetranslator1.morse_encryptor(text),expected_output)
    
    def test_encryption_with_numbers_characters(self):
        text= "Jana1910?."
        expected_output= ".--- .- -. .- .---- ----. .---- ----- ..--.. .-.-.-"
        self.assertEqual(morsetranslator1.morse_encryptor(text),expected_output)

    def test_decryption_without_space(self):
        text= ".--- .- -. .-"
        output= "JANA"
        self.assertEqual(morsetranslator1.morse_decryptor(text), output)
    
    def test_decryption_with_spaces(self):
        text= ".--- .- -. .- / .-- .- ... / .... . .-. ."
        output= "JANA WAS HERE"
        self.assertEqual(morsetranslator1.morse_decryptor(text),output)
    
    def test_decryption_numbers_characters(self):
        text= ".--- .- -. .- .---- ----. .---- ----- ..--.. .-.-.-"
        output="JANA1910?."
        self.assertEqual(morsetranslator1.morse_decryptor(text),output)
    

        


if __name__ == '__main__':
    unittest.main()
