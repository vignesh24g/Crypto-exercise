import sys

def decrypt(plain_text,key) -> str:
    result = ""
    # traverse text
    for i in range(len(plain_text)):
        char = plain_text[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + key+65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key + 97) % 26 + 97)
    return result

if __name__=="__main__":
    if(len(sys.argv) <3):
        print("Enter the ciphertext file and space key to shift")
        exit(0)

    with open(sys.argv[1],"r") as f:
        cipher_text=f.read()

    key=sys.argv[2]

    plain_text=decrypt(cipher_text,int(key))
    
    with open("decrypted_text.txt","w") as f:
        f.write(plain_text)