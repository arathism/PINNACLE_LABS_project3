# Image Encryption — Secure File Encryption Tool

A Python CLI tool that encrypts and decrypts image files, built as part of the Pinnacle Labs Cybersecurity Internship, to protect visual data from unauthorized access and tampering.

## Important

- Encryption/decryption happens entirely on your own machine — no network calls, no data leaves your device
- Never overwrites your original image; it always writes to a separate output file
- A lost or changed key file means the encrypted image can never be decrypted — back up `key.key` somewhere safe
- Decryption will fail loudly (not silently corrupt) if the wrong key or a tampered file is used

## Requirements

```
pip install cryptography
```

## Usage

```
python image_encryption.py genkey key.key
python image_encryption.py encrypt input.jpg encrypted.bin key.key
python image_encryption.py decrypt encrypted.bin decrypted.jpg key.key
```

1. Generate a key once with `genkey` — keep this file safe, it's required for both encrypting and decrypting.
2. Encrypt any image with `encrypt`, pointing to the real filename (quote it if it has spaces, e.g. `"my photo.jpg"`).
3. Decrypt with `decrypt`, using the same key, to get the original image back.

## How It Works

- Uses `Fernet` (AES-128 in CBC mode with HMAC authentication, from Python's `cryptography` library) to encrypt the raw bytes of the file
- Because it works on raw bytes, any image format (JPG, PNG, BMP, etc.) is supported
- The HMAC authentication tag means a tampered or corrupted encrypted file, or the wrong key, is detected and rejected on decryption rather than producing a silently broken image

## Example Run

```
PS> python image_encryption.py genkey key.key
[+] New key generated and saved to 'key.key'

PS> python image_encryption.py encrypt "images (1).jpeg" encrypted.bin key.key
[+] Image 'images (1).jpeg' encrypted successfully -> 'encrypted.bin'

PS> python image_encryption.py decrypt encrypted.bin decrypted.jpeg key.key
[+] Image decrypted successfully -> 'decrypted.jpeg'
```
`decrypted.jpeg` was verified identical to the original source image.

## Defensive Takeaways

- Always encrypt sensitive images at rest, not just in transit
- A strong, properly generated key (not a guessable password) is what actually protects the data — the algorithm is only as strong as key handling
- Authenticated encryption (like Fernet's HMAC) catches tampering that plain encryption would miss
- Never hardcode or commit encryption keys to source control

## Author

Arathi Shekhar Munavalli
