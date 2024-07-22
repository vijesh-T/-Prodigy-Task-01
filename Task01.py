

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text,shift_key): #hello h=7
    cipher_text=""
    for char in plain_text:
        position=alphabet.index(char)
        new_position=(position+shift_key)%26
        cipher_text +=alphabet[new_position]
    print(f"Here's is the text after encryption: {cipher_text}")

def decryption(cipher_text,shift_key): #khoor
    plain_text=""
    for char in cipher_text: #char=k
        position=alphabet.index(char)
        new_position=(position-shift_key)%26
        plain_text +=alphabet[new_position]
    print(f"Here's is the text after decryption: {plain_text}")

end=False
while not end:
    what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text=input("Type your message:\n")
    shift=int(input("Enter shift key:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
        print("Encryption Complete")
    elif what_to_do=="decrypt":
        decryption(text,shift)
        print("Decryption Complete")
    play_again=input("Would you like to play again?(y/n)\n")
    if play_again=='n':
        end=True
        print("Thank you for playing")
