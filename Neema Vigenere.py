def vigenere_cipher(text, key):
    key = key.lower()
    key_length = len(key)
    ciphertext = ""

    for i, char in enumerate(text):
        if char.isalpha():
            if char.isupper():
                shift = ord(key[i % key_length]) - 97
                ciphertext += chr(((ord(char) - 65 + shift) % 26) + 65)
            else:
                shift = ord(key[i % key_length]) - 97
                ciphertext += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            ciphertext += char

    return ciphertext

plaintext = "neema"
keyword = "Brain"
ciphertext = vigenere_cipher(plaintext, keyword)

print("Plaintext:", plaintext)
print("Keyword:", keyword)
print("Ciphertext:", ciphertext)
