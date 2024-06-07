from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Encrypt by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256

    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Decrypt by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256

    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

def main():
    print("Image Encryption and Decryption Tool")
    
    while True:
        choice = input("Choose an option:\n1. Encrypt an image\n2. Decrypt an image\n3. Exit\n")
        
        if choice == '1':
            input_image_path = input("Enter the path of the image to encrypt: ")
            output_image_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(input_image_path, output_image_path, key)
        
        elif choice == '2':
            input_image_path = input("Enter the path of the image to decrypt: ")
            output_image_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(input_image_path, output_image_path, key)
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
