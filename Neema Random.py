import random

def generate_substitution_key():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

def random_substitution_cipher(text, substitution_key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += substitution_key.get(char.lower(), char).upper()
            else:
                result += substitution_key.get(char, char)
        else:
            result += char
    return result

plaintext = "neema"
substitution_key = generate_substitution_key()
ciphertext = random_substitution_cipher(plaintext, substitution_key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
