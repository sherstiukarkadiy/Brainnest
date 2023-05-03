from logical_functions import *

variations_dict = {
    "encrypt": encrypt,
    "decrypt": decrypt
}

def create_menu(dict: dict) -> str:
    """Create menu with difficulty levels

    Args:
        dict (dict): Variations dictionary

    Returns:
        str: menu
    """
    header = "|{:^14}|".format("Menu")
    spliter = "-"*16
    board = ""
    num = 1
    for level in dict:
        board += "|{:^3}|{:^10}|\n".format(num, level)
        num += 1
    menu = f"{spliter}\n{header}\n{spliter}\n{board}{spliter}"
    return menu

print(create_menu(variations_dict))
wait_for_key = False
while True:
    if not wait_for_key:
        cryption = input("Choose what to do\n>")
        if invalid_input_check(cryption,wait_for_key): continue
        cryption = list(variations_dict.keys())[int(cryption)-1]
        wait_for_key = True
    
    if wait_for_key:
        key_value = input("Please enter the key (0 to 25) to use.\n>")
        if invalid_input_check(key_value,wait_for_key): continue
        key_value = int(key_value)
        wait_for_key = False
    break