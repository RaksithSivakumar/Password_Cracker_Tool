import itertools
import string
import time
import os

# Create logs folder if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Brute-force attack function
def brute_force_attack(target_password):
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
    attempts = 0
    start_time = time.time()
    
    with open("logs/attack_logs.txt", "a") as log_file:
        log_file.write(f"\nBrute Force Attack started on {target_password}\n")
        
        for password_length in range(1, 9):  # Limit length to 8 for simplicity
            for guess in itertools.product(charset, repeat=password_length):
                attempts += 1
                guess = ''.join(guess)
                if guess == target_password:
                    end_time = time.time()
                    log_file.write(f"Password cracked: {guess} in {attempts} attempts. Time: {end_time - start_time:.2f} seconds\n")
                    return f"Password cracked: {guess} in {attempts} attempts. Time: {end_time - start_time:.2f} seconds"
                
                log_file.write(f"Trying password: {guess}\n")

    return "Password not found in brute force attack."

# Dictionary attack function
def dictionary_attack(target_password, dictionary_file='password_list.txt'):
    attempts = 0
    start_time = time.time()

    try:
        with open(dictionary_file, 'r') as file, open("logs/attack_logs.txt", "a") as log_file:
            log_file.write(f"\nDictionary Attack started on {target_password}\n")
            
            for line in file:
                attempts += 1
                password_guess = line.strip()
                if password_guess == target_password:
                    end_time = time.time()
                    log_file.write(f"Password cracked using dictionary: {password_guess} in {attempts} attempts. Time: {end_time - start_time:.2f} seconds\n")
                    return f"Password cracked using dictionary: {password_guess} in {attempts} attempts. Time: {end_time - start_time:.2f} seconds"
                
                log_file.write(f"Trying password: {password_guess}\n")

    except FileNotFoundError:
        return f"Error: Dictionary file '{dictionary_file}' not found."

    return "Password not found in dictionary attack."
