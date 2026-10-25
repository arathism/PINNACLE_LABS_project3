"""
Image Encryption Tool
----------------------
Encrypts and decrypts image files using Fernet (AES-128 in CBC mode with
HMAC authentication, via the 'cryptography' library). Works on any image
format (png, jpg, bmp, etc.) since it just encrypts the raw bytes.

Install dependency first:
    pip install cryptography

Usage:
    python image_encryption.py encrypt input.png encrypted.bin key.key
    python image_encryption.py decrypt encrypted.bin decrypted.png key.key
    python image_encryption.py genkey key.key
"""

import sys
import os
from cryptography.fernet import Fernet


def generate_key(key_path: str) -> None:
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
    print(f"[+] New key generated and saved to '{key_path}'")


def load_key(key_path: str) -> bytes:
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file '{key_path}' not found. Run 'genkey' first.")
    with open(key_path, "rb") as f:
        return f.read()


def encrypt_image(input_path: str, output_path: str, key_path: str) -> None:
    key = load_key(key_path)
    fernet = Fernet(key)

    with open(input_path, "rb") as f:
        image_data = f.read()

    encrypted_data = fernet.encrypt(image_data)

    with open(output_path, "wb") as f:
        f.write(encrypted_data)

    print(f"[+] Image '{input_path}' encrypted successfully -> '{output_path}'")


def decrypt_image(input_path: str, output_path: str, key_path: str) -> None:
    key = load_key(key_path)
    fernet = Fernet(key)

    with open(input_path, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print(f"[!] Decryption failed: {e}")
        print("    (Wrong key or corrupted/tampered file.)")
        return

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

    print(f"[+] Image decrypted successfully -> '{output_path}'")


def print_usage():
    print(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "genkey":
        if len(sys.argv) != 3:
            print("Usage: python image_encryption.py genkey key.key")
            sys.exit(1)
        generate_key(sys.argv[2])

    elif command == "encrypt":
        if len(sys.argv) != 5:
            print("Usage: python image_encryption.py encrypt input.png encrypted.bin key.key")
            sys.exit(1)
        encrypt_image(sys.argv[2], sys.argv[3], sys.argv[4])

    elif command == "decrypt":
        if len(sys.argv) != 5:
            print("Usage: python image_encryption.py decrypt encrypted.bin decrypted.png key.key")
            sys.exit(1)
        decrypt_image(sys.argv[2], sys.argv[3], sys.argv[4])

    else:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)