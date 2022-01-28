# This program will translate from normal language to Vernon-Lopez code

HALF_1 = "ABCDEFGHIJKLM"
HALF_2 = "NOPQRSTUVWXYZ"
ALPHABET = HALF_1 + HALF_2 

def translate_word(normal_word):
    """
    Input: word in normal language (no spaces)
    Output: word in VL code
    
    >>> w = "aaaa"
    >>> new_w = translate_word(w)
    >>> print(new_w)
    OPQR
    
    >>> v = "hola"
    >>> new_v = translate_word(v)
    >>> print(new_v)
    VDBR
    """
    
    vl_word = ""
    
    # initialize an index that will signal the position of a letter within the word
    i = 1
    
    for c in normal_word.upper():
        
        # Get position of each letter.
        pos = ALPHABET.index(c)
        
        # Add 13 to translate to other column. Add the respective position within the word -- the complexity touch.
        pos += 13 + i
        
        # Calculate modulo 26, so that any larger number will be brought back to the working space 1-26.
        pos = pos % 26
        
        # Add the new, encrypted character to vl_word       
        vl_word += ALPHABET[pos]
        
        # Increment i
        i += 1
        
    # Output: return the encrypted word
    return vl_word

def decrypt_word(VL_word):
    
    decrypted_word = ""
    
    # initialize an index that will signal the position of a letter within the word
    i = 1
    
    for c in VL_word.upper():
        
        # Get position of each letter.
        pos = ALPHABET.index(c)
        
        # Subtract 13 to translate to other column. Subtract the respective position within the word -- the complexity touch.
        pos = pos - 13 - i
        
        # Calculate modulo 26, so that any smaller number will be brought back to the working space 1-26.
        pos = pos % 26
        
        # Add the new, encrypted character to vl_word       
        decrypted_word += ALPHABET[pos]
        
        # Increment i
        i += 1
        
    # Output: return decrypted word
    return decrypted_word

def encrypt_sentence(input_txt):
    """ (str) -> str
    Encrypts a sentence word by word, by replacing spaces by "Σ"
    """
    
    word_list = input_txt.split()
    encrypted_word_list = []
    encrypted_str = ""
    
    # Encrypt each word
    for word in word_list:
        
        encrypted_word = translate_word(word)
        
        encrypted_word_list.append(encrypted_word)
        
    for elem in encrypted_word_list:
        
        encrypted_str += elem
        
        encrypted_str += 'Σ'
        
    # Output
    return encrypted_str

def decrypt_sentence(input_txt):
    """ (str) -> str
    Decrypts from VL code to normal language.
    
    >>> w = "VDBRΣVDBR"
    >>> v = decrypt_sentence(w)
    >>> print(v)
    HOLA HOLA 
    """
    word_list = input_txt.split('Σ')
    decrypted_word_list = []
    decrypted_str = ""
    
    # Decrypt each word
    for word in word_list:
        
        decrypted_word = decrypt_word(word)
        
        decrypted_word_list.append(decrypted_word)
        
    for elem in decrypted_word_list:
    
        decrypted_str += elem
    
        decrypted_str += ' ' 
    
    return decrypted_str

def run_program():
    
    mode = input("Welcome!\n1: Normal -> VL\n2: VL -> Normal\n\n Enter your mode: ")
    
    if mode == "1":
    
        input_txt = input("Enter the word or phrase you desire to code into VL code:\n")
        
        encrypted_txt = encrypt_sentence(input_txt)
        
        print(encrypted_txt)
        
    if mode == "2":
    
        input_txt = input("Enter the word or phrase you desire to turn back into normal language:\n")
        
        decrypted_txt = decrypt_sentence(input_txt)
        
        print(decrypted_txt)
    
if __name__ == "__main__":
    run_program()
