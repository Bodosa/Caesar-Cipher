from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

should_continue = True



'''
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        encrypted_text = alphabet.index(letter) + shift_amount
        encrypted_text = encrypted_text % len(alphabet)  # to get back to
        cipher_text += alphabet[encrypted_text]

    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        decrypted_text = alphabet.index(letter) - shift_amount
        decrypted_text = decrypted_text % len(alphabet)
        output_text += alphabet[decrypted_text]

    print(f"Here is the decoded result: {output_text}")

'''


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            decrypted_text = alphabet.index(letter) + shift_amount
            decrypted_text = decrypted_text % len(alphabet)
            output_text += alphabet[decrypted_text]

    print(f"Here is the {encode_or_decode} result: {output_text}")


# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)
while should_continue:
    decision = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message\n").lower()
    shift = int(input("Type the shift number\n"))
    caesar(text, shift, decision)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")

