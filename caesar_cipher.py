def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

if choice == 'E':
    print("Encrypted message:", encrypt(message, shift))
elif choice == 'D':
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice!")
