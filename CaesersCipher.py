def encrypt(text, shift):
    """Encrypt the text using the Caesar Cipher algorithm."""
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # non-alphabetical characters remain the same
    
    return result

def decrypt(text, shift):
    """Decrypt the text using the Caesar Cipher algorithm."""
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    while True:
        choice = input("Choose an option:\n1. Encrypt a message\n2. Decrypt a message\n3. Exit\n")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
