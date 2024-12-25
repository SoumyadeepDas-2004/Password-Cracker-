import itertools # generates combinations of a given set of characters
import hashlib # generates hash values of the given password
import time # to access current time

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()  # returns the hash value of the password in hexadecimal format

# Dictionary attack function
def dictionary_attack(hash_to_crack, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for word in file:  # iterates over each line in the dictionary file
            word = word.strip()  # Remove any leading/trailing whitespace
            attempt_hash = hash_password(word)
            if attempt_hash == hash_to_crack:  # Check if the hash of the dictionary word matches the hash of the password
                return word
    return None  # Return None if no match is found in the dictionary

# Brute-force attack function
def brute_force_attack(hash_to_crack, charset, max_length):
    start_time = time.time()
    for length in range(1, max_length + 1):
        print(f"Trying passwords of length {length}...")
        for attempt in itertools.product(charset, repeat=length):  # generates all possible combinations of the given charset for the given length
            attempt_password = ''.join(attempt)  # joins the characters to form a password (string)
            attempt_hash = hash_password(attempt_password)  # hashes the generated test password
            if attempt_hash == hash_to_crack:  # checks if the hash value of the generated password matches the hash value of the password to crack
                end_time = time.time()
                print(f"Password cracked: {attempt_password}")
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return attempt_password
    print("Password not found within the given length.")
    return None

# Example usage
if __name__ == "__main__":  # entry point of the program
    # Set the password to crack
    print("Enter the password to crack: ")
    real_password = input().strip()  # Read password and delete any front and end white spaces if any
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#-_~"  # most common Character set to try
    max_length = 12  # Maximum length of password to attempt

    # Hash the password
    hashed_password = hash_password(real_password)  # Hash the real password
    print(f"Hashed password: {hashed_password}")

    # First, attempt the dictionary attack
    dictionary_file = 'python\passcrack\common_passwords.txt'  #path to the dictionary file
    print("Attempting dictionary attack...")
    cracked_password = dictionary_attack(hashed_password, dictionary_file)  # Attempt dictionary attack

    if cracked_password:  # If dictionary attack is successful
        print(f"Password cracked by dictionary attack: {cracked_password}")
    else:
        # If dictionary attack fails, proceed with brute-force attack
        print("Dictionary attack failed. Proceeding with brute-force attack...")
        cracked_password = brute_force_attack(hashed_password, charset, max_length) # Attempt brute force attack

    if cracked_password:  # If the password is cracked by either method
        print(f"Successfully cracked the password: {cracked_password}")
    else:
        print("Failed to crack the password.")
