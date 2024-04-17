import string 

def ceasar_encrypt(message , key):

    shift = key%26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:]+ string.ascii_lowercase[:shift])
    # basically a keyvalue pair kind of stuff
    # for a = string.ascii_lowercase - abcdefghijklmnopqrstuvwxyz
    # for shift: - cdefghijklmnopqrstuvwxyz
    # for :shift - abc
    # for b = shift: + :shift - cdefghijklmnopqrstuvwxyzabc
    # so a is mapped with b using translational table 

    encrypted_message = message.lower().translate(cipher)

    return encrypted_message

def ceasar_decrypt(encrypted_message,key):

    shift = 26 - (key%26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:]+ string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

message = 'Hello My Name is Danien'
key = 3 

encrypted_message = ceasar_encrypt(message ,key )
print(f'Encrypted message:{encrypted_message}')

decrypted_message = ceasar_decrypt(encrypted_message,key)
print(f'Decrypted message:{decrypted_message}')

