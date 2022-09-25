import sys
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#The methode to do frequency analysis : we just count the occurrences of the given characters
def frequency_analysis(cipher_text):
    cipher_text = cipher_text.upper()
    letter_frequencies = {}

    #Initialize the dictionary (of course with 0 frequencies)
    for letter in LETTERS :
        letter_frequencies[letter] = 0

    for letter in cipher_text:
        #We keep incrementing the occurence of the given letter
        if letter in LETTERS:
            letter_frequencies[letter]+=1
    return letter_frequencies

def caesar_crack(cipher_text):
    frequency= frequency_analysis(cipher_text)
    print(frequency)
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse = True )
    print("\nHere is the frequency sorted : ")
    print(frequency)
    #To find the letter with the  second highest frequency
    print("\nThe possible key value is : %s" % (LETTERS.find(frequency[1][0]) - LETTERS.find('E')))

if __name__ == '__main__':
    if(len(sys.argv) <2):
        print("Enter the cipher text file")
        exit(0)

    with open(sys.argv[1],"r") as f:
        cipher_text=f.read()

    caesar_crack(cipher_text) #Information Leaking in this cryptosystem, because the most used letter in the english alphabet is E.
                              #So we know that the most used letter crypted corresponds to E, in our case it's H.
                              #Therefore we will immediatly know the key used for crypting, which is 3.