def decrypt(text,s):
    print("Enter 1 to encrypt a word\nEnter 2 to decrypt a word")
    n=int(input())
    # Cipher(n) = De-cipher(26-n)

    s=26-s
        
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):  #if the text[i] is in upper case
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result


word=str(input("enter the word:"))
d=int(input("Enter the key: "))

print("Encoded word in Caeser cipher is: ",decrypt(word,d))

