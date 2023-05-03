from logical_functions import *

message = input(f"Enter the message to decrypt\n>")
for i in range(26):
    result = decrypt(message, i)
    print("Key {:>2}: ".format(i), end="") 
    print (result)

