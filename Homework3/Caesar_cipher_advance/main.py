from menu_functions import *

message = input(f"Enter the message to {cryption}\n>")
result = variations_dict[cryption](message, key_value)
print (result)
