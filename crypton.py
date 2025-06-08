import base64
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()

def encrypt_password(password: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return base64.urlsafe_b64encode(encrypted).decode()

def decrypt_password(token: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted = base64.urlsafe_b64decode(token.encode())
    return f.decrypt(encrypted).decode()

if __name__ == "__main__":
    # Generate and save key
    key = generate_key()
    print(f"This is your Encryption Key, make sure to save it: {key.decode()}.")

    # Encrypt password
    password = input("Enter password to encrypt: ")
    encrypted = encrypt_password(password, key)
    print(f"Encrypted password: {encrypted}")

    # Decrypt password
    to_decrypt = input("Enter encrypted password to decrypt: ")
    decrypted = decrypt_password(to_decrypt, key)
    print(f"Decrypted password: {decrypted}")
