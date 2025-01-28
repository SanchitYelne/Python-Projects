from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    shift %= 25
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"Encrypted cipher text is : {cipher_text}")


def decrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        if letter == " ":
            cipher_text += letter
        elif new_position < 0:
            new_position = 26 + new_position
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"Decrypted cipher text is : {cipher_text}")


play = True

while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:, type 'exit' to exit: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    elif direction == "exit":
        exit()




