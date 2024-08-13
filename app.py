from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    pixels = list(image.getdata())
    
    # Encrypt the image by applying a simple operation on each pixel value
    encrypted_pixels = [(pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key) for pixel in pixels]

    # Create a new image with the encrypted pixel values
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(encrypted_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(encrypted_image_path)
    pixels = list(image.getdata())
    
    # Decrypt the image by applying the reverse operation on each pixel value
    decrypted_pixels = [(pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key) for pixel in pixels]

    # Create a new image with the decrypted pixel values
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

# Example usage:
key = 123  # Simple key for XOR operation
encrypt_image('input.jpg', 'encrypted_image.png', key)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)
