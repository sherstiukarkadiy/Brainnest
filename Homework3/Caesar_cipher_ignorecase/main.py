from functions import *

wait_for_key = False
while True:
    if not wait_for_key:
        cryption = input("Do you want to (e)ncrypt or (d)ecrypt?\n>").lower()
        if invalid_input_check(cryption,wait_for_key): continue
        if cryption == "e": cryption = "encrypt"
        else: cryption = "decrypt"
        wait_for_key = True
    
    if wait_for_key:
        key_value = input("Please enter the key (0 to 25) to use.\n>")
        if invalid_input_check(key_value,wait_for_key): continue
        key_value = int(key_value)
        wait_for_key = False
    break

message = input(f"Enter the message to {cryption}\n>")
if cryption == "encrypt":
    result = encrypt(message, key_value)
else:
    result = decrypt(message, key_value)
print (result)
