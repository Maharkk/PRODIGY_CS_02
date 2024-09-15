from PIL import Image
import numpy as np
import os

def load_image(image_path):
    """Loads an image from the file system."""
    if not os.path.exists(image_path):
        print(f"File '{image_path}' not found. Please specify the correct file.")
        return None
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode
    return img

def save_image(img, output_path):
    """Saves the image to the file system in PNG format to avoid compression artifacts."""
    img.save(output_path, format='PNG')  # Saving as PNG to avoid lossy compression

def encrypt_image(img, key):
    """Encrypts the image by applying an XOR operation on each pixel using the key."""
    img_array = np.array(img)
    
    # Apply XOR operation using the key and ensure pixel values stay in valid range (0-255)
    encrypted_array = (img_array ^ key) % 256  
    
    # Debug: Print some of the original and encrypted pixels for verification
    print("\nOriginal pixel values (sample):", img_array[0, 0])
    print("Encrypted pixel values (sample):", encrypted_array[0, 0])
    
    # Convert back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'), 'RGB')
    return encrypted_img

def decrypt_image(encrypted_img, key):
    """Decrypts the image by applying the XOR operation again using the provided key."""
    return encrypt_image(encrypted_img, key)

def compare_images(img1, img2):
    """Compares the pixel values of two images."""
    array1 = np.array(img1)
    array2 = np.array(img2)
    
    # Compare the two arrays
    return np.array_equal(array1, array2)

def user_menu():
    print("What would you like to do with an image?")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1 or 2): ")
    return choice

# Main execution
if __name__ == "__main__":
    choice = user_menu()

    if choice == "1":
        # Encrypt the image
        image_path = input("\nEnter the path of the image you want to encrypt: ")
        img = load_image(image_path)
        
        if img is not None:
            key = int(input("Enter the key for encryption: "))
            encrypted_img = encrypt_image(img, key)
            encrypted_output_path = input("\nEnter the output path for the encrypted image (e.g., encrypted_image.png): ")
            save_image(encrypted_img, encrypted_output_path)
            print("\nThe image has been successfully encrypted and saved as:", encrypted_output_path)
    
    elif choice == "2":
        # Decrypt the image
        encrypted_image_path = input("\nEnter the path of the encrypted image you want to decrypt: ")
        encrypted_img = load_image(encrypted_image_path)
        
        if encrypted_img is None:
            print("Encrypted image not found. Please specify the correct file.")
        else:
            key = int(input("Enter the key for decryption: "))
            decrypted_img = decrypt_image(encrypted_img, key)
            decrypted_output_path = input("\nEnter the output path for the decrypted image (e.g., decrypted_image.png): ")
            save_image(decrypted_img, decrypted_output_path)
            
            # Load the original image to compare
            original_image_path = input("Enter the path of the original image for comparison (optional, or press Enter to skip): ")
            if original_image_path and os.path.exists(original_image_path):
                original_img = load_image(original_image_path)
                
                if compare_images(original_img, decrypted_img):
                    print("\nDecryption successful! The image has been successfully decrypted and saved as:", decrypted_output_path)
                else:
                    print("\nDecryption failed. The decrypted image does not match the original image.")
            else:
                print("\nDecryption completed and saved as:", decrypted_output_path)
    
    else:
        print("\nInvalid choice. Please select 1 for encryption or 2 for decryption.")
