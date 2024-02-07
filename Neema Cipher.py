def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

plaintext = "Neema"
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
