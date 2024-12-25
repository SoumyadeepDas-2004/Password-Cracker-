# Password-Cracker-
I made a password cracker tool using Python

This repository contains a Python program that demonstrates two methods of cracking a hashed password: **Dictionary Attack** and **Brute-Force Attack**. The program takes a password hash (SHA-256) and attempts to crack it using a dictionary file of common passwords or by brute-forcing all possible combinations within a specified length and character set.

## Features

- **Dictionary Attack**: Tries passwords from a predefined dictionary (a file containing common passwords).
- **Brute-Force Attack**: Generates all possible combinations of a specified character set for passwords of different lengths.

## Requirements

- Python 3.x
- `hashlib` library (included in Python by default)

## How it Works

1. **Dictionary Attack**: The program will first try to crack the password by comparing the hash with each word from a dictionary file (e.g., `common_passwords.txt`).
2. **Brute-Force Attack**: If the dictionary attack fails, the program will attempt all possible combinations of characters (letters, numbers, and special characters) up to a specified maximum length.
