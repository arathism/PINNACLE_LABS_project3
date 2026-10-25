# Image Encryption

**Category:** Cybersecurity — Pinnacle Labs Internship (2026)

## Description
Create a tool to secure image files with encryption, protecting visual data from unauthorized access and tampering.

## How It Works
This tool uses **Fernet** (AES-128 in CBC mode with HMAC authentication, from Python's `cryptography` library) to encrypt and decrypt the raw bytes of an image file. Because it operates on bytes, it works with any image format (PNG, JPG, BMP, etc.).

## Requirements
```bash
pip install cryptography
```

## Usage
```bash
# 1. Generate an encryption key (do this once, keep the key file safe)
python image_encryption.py genkey key.key

# 2. Encrypt an image
python image_encryption.py encrypt input.jpg encrypted.bin key.key

# 3. Decrypt it back
python image_encryption.py decrypt encrypted.bin decrypted.jpg key.key
```
Replace `input.jpg` with your actual image filename (quote it if the name has spaces, e.g. `"my photo.jpg"`).

## Example Run
```
PS> python image_encryption.py genkey key.key
[+] New key generated and saved to 'key.key'

PS> python image_encryption.py encrypt "images (1).jpeg" encrypted.bin key.key
[+] Image 'images (1).jpeg' encrypted successfully -> 'encrypted.bin'

PS> python image_encryption.py decrypt encrypted.bin decrypted.jpeg key.key
[+] Image decrypted successfully -> 'decrypted.jpeg'
```
`decrypted.jpeg` is verified identical to the original source image.

## Features
- AES-128 encryption with built-in integrity verification (HMAC)
- Works with any image file format
- Simple CLI: generate key, encrypt, decrypt
- Detects tampered/corrupted files or wrong keys on decryption

## Author
Arathi Shekhar Munavalli