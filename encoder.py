def encode(string,key):
    new=''
    for ig in string:
        new+=chr(ord(ig)+key)
    return new


ascii_art_string="""  __  __  _             _       
 |  \/  |(_)           (_)      
 | \  / | _  _ __ ___   _  _ __ 
 | |\/| || || '_ ` _ \ | || '__|
 | |  | || || | | | | || || |   
 |_|  |_||_||_| |_| |_||_||_|   
"""

print(ascii_art_string)
string = input("Enter a string to be encoded: ")
key = int(input("Enter a key for the string: "))
print("The encoded string is: ", encode(string,key))
