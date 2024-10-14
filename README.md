# Password Cracker Tool
A password cracking tool built with Python, using Brute Force and Dictionary attack methods. The project also includes a Streamlit frontend for ease of use and logs all cracking attempts.

## Table of Contents
Overview

Features

Project Structure

Installation

Usage

Inputs

Technologies Used

Logging

Future Enhancements

Contributing


## Overview
The Password Cracker Tool is designed to simulate password cracking using two common techniques:

1. Brute Force Attack: Tries every possible combination of characters to guess the password.

2. Dictionary Attack: Tries to match the password using a list of common passwords.
The tool also includes a Streamlit user interface that makes it easy to select an attack type, input a target password, and view results. All attempts are logged in a logs/attack_logs.txt file.

## Features
1.Brute Force Attack: Attempts to crack passwords by trying all possible combinations.

2.Dictionary Attack: Uses a predefined list of common passwords to attempt cracking.

3.Streamlit Frontend: A user-friendly interface for input and interaction.

4.Logging: Every password attempt is logged in a file for analysis.

5.Customizable Dictionary: You can easily update the dictionary list (password_list.txt) to include more passwords for testing.

## Project Structure
```bash
Copy code
Password_Cracker_Tool/
│
├── app.py                  # Streamlit frontend
├── attack.py               # Core logic for the brute force and dictionary attacks
├── password_list.txt        # List of common passwords for dictionary attack
├── logs/                    # Folder to store log files
│   └── attack_logs.txt      # Log file to store password cracking attempts
├── utils/                   # Utility functions for attack handling
│   └── logger.py            # Logging functions
└── README.md                # Project README
```
Installation
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Clone the Repository
```bash
Copy code
git clone https://github.com/your-username/password_cracker_tool.git
```
```bash
cd password_cracker_tool
```
### Install Dependencies
Install the required packages using pip:

```bash
Copy code
pip install -r requirements.txt
```
## Required Libraries
streamlit: For frontend interface.

hashlib: For hash-based comparison (used in password cracking).

itertools: For generating character combinations (brute force).

os, time, logging: For file operations and logging.

sys: For basic system operations.

## Usage
Running the Application
To run the Password Cracker Tool with the Streamlit frontend, use the following command:

```bash
Copy code
streamlit run app.py
```
This will open the Streamlit interface in your web browser, where you can interact with the tool.

## Steps to Use
Open Streamlit: After running streamlit run app.py, the interface will open in your default browser.

Enter the Target Password: Provide the password you want to crack.

Select Attack Type: Choose between "Brute Force Attack" or "Dictionary Attack."

Click "Start Cracking": The cracking process will begin, and results will be displayed.

View Results: The cracked password (if found) and the number of attempts are shown in the output.

## Inputs
1.Password Field: Enter the password you want to test for cracking. Example: password123.

#### Attack Selection: Choose between:
1.Brute Force Attack: Attempts all possible combinations.

2.Dictionary Attack: Uses words from the password_list.txt file.

## Technologies Used
1.Python: Core programming language.

2.Streamlit: For building the frontend interface.

3.Logging: Built-in Python library for logging events and actions.

4.Cryptography Concepts: Basic concepts for secure password handling.

## Logging
1.All attempts made by the password cracker tool are logged for later analysis. Logs include:

2.Timestamp of the cracking attempt.

3.Password tried.

4.Attack type used (Brute Force or Dictionary).

5.Success or failure message.

## Log Location
Logs are stored in:

```bash
Copy code
logs/attack_logs.txt
```
## Sample Log Entry txt
```bash
Copy code
[2024-10-14 10:15:32] Attempted to crack 'admin' using Dictionary Attack. Success!
```
## Future Enhancements
1.Hash Cracking: Add functionality to crack hashed passwords (MD5, SHA-256, etc.).

2.Multi-threading: Improve performance by enabling parallel processing.

3.Enhanced Dictionary: Expand the dictionary to include more common passwords.

4.Real-Time Monitoring: Show real-time progress updates in the Streamlit UI.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or file an issue in the repository. We welcome improvements and bug fixes.

