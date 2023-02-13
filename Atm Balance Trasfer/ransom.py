import cryptography
from cryptography.fernet import Fernet

def encrypt_file(file_name, password):
    # Generate a key from the password
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(file_name, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    # Write the encrypted data to a new file
    with open(file_name + ".encrypted", 'wb') as file:
        file.write(encrypted_data)

    # Store the key in a separate file
    with open("key.key", 'wb') as key_file:
        key_file.write(key)

def decrypt_file(file_name, password):
    # Load the key from the key file
    with open("key.key", 'rb') as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    # Load the encrypted data from the file
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data to a new file
    with open(file_name + ".decrypted", 'wb') as file:
        file.write(decrypted_data)

def main():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice: ")
    file_name = input("Enter the file name: ")
    password = input("Enter the password: ")
    if choice == '1':
        encrypt_file(file_name, password)
    elif choice == '2':
        decrypt_file(file_name, password)

if __name__ == '__main__':
    main()
