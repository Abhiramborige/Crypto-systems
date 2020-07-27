def encrypt(text,s):
   
    # Cipher(n) = De-cipher(26-n)
    s=s   
    text =text.replace(" ","")
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):  #if the text[i] is in upper case
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result


word=str(input("enter the word:"))
k=int(input("Enter the key: "))

print("Encoded word in Caeser cipher is: ",encrypt(word,k))

'''
----------OUTPUT----------
enter the word:hi there my name is abhiram
Enter the key: 3
Encoded word in Caeser cipher is:  klwkhuhpbqdphlvdekludp
>>> 
'''
