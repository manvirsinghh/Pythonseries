print("ENCRYPTION/DECRYPTION")

# Function to encrypt the message
def encrypt(message, shift_position):
    encrypted_message = ""
    for i in message:
        position = ord(i)  # Get the ASCII value of the character
        encrypted_message += chr(position + shift_position)  # Shift and append to result
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, shift_position):
    decrypted_message = ""
    for i in encrypted_message:
        position = ord(i)  # Get the ASCII value of the character
        decrypted_message += chr(position - shift_position)  # Shift back and append to result
    return decrypted_message  # Return the decrypted message

# User input
message = input("Enter the message: ")
shift_position = int(input("Enter the number with which you want to shift the letter: "))
choice = int(input("Enter your choice here (1 for encryption, 2 for decryption): "))

if choice == 1:
    encrypted = encrypt(message, shift_position)  # Encrypt the message
    print(f"Encrypted message is: {encrypted}")
    # Now decrypt the message immediately after encryption
    decrypted = decrypt(encrypted, shift_position)
    print(f"Decrypted message is: {decrypted}")
elif choice == 2:
    decrypted = decrypt(message, shift_position)  # Decrypt the message directly
    print(f"Decrypted message is: {decrypted}")
else:
    print("Enter a valid choice (1 for encryption, 2 for decryption).")
