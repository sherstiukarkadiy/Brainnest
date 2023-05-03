def encrypt(message: str,offset: int) -> str:
    """Encrypting a message

    Args:
        message (str): Sentense you want to encrypt
        offset (int): Value to offset

    Returns:
        str: encrypted message
    """
    encrypted_message = ""
    for ch in message:
        if not ch.isalpha():
            encrypted_message+=ch
        elif "a"<=ch<="z":
            pos = ord(ch) - ord('a') 
            pos = (pos+offset)%26
            encrypted_message+=chr(ord('a')+ pos)
        else:
            pos = ord(ch) - ord('A') 
            pos = (pos+offset)%26
            encrypted_message+=chr(ord('A')+ pos)
    return encrypted_message

def decrypt(message: str,offset: int) -> str:
    """Decrypting a message

    Args:
        message (str): Sentense you want to encrypt
        offset (int): Value to offset

    Returns:
        str: decrypted message
    """
    decrypted_message = ""
    for ch in message:
        if not ch.isalpha():
            decrypted_message+=ch
        elif "a" <= ch <= "z":
            pos = ord("z") - ord(ch) 
            pos = (pos+offset)%26
            decrypted_message+=chr(ord('z') - pos)
        else:
            pos = ord("Z") - ord(ch) 
            pos = (pos+offset)%26
            decrypted_message+=chr(ord('Z') - pos)
    
    return decrypted_message

def invalid_input_check(variable: str, wait_for_key: bool) -> bool:
    """Check if user input is correct

    Args:
        variable (str): user input variable;
        wait_for_key (bool): the boolin flag to know what to chek: digits between 0 and 25 if True or digints 1 or 2 if False;

    Returns:
        bool: True if input is invalid, else - False
    """
    if wait_for_key:
        if variable.isdigit() and 0 <= int(variable) <= 25:
            return False
    else:
        if variable.isdigit() and 0 < int(variable) <= 2:
            return False
    print("Invald input")
    return True