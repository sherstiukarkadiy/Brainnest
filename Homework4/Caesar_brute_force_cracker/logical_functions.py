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

