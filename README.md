# BF: Instagram Password Cracker
# Developed And Designed By Muhammad Hammad Haider

## Description

- BF is a Python script designed for ethical purposes to perform brute-force attacks on Instagram accounts, allowing users to recover forgotten or lost passwords. This script utilizes a list of possible passwords and various techniques to attempt to gain access to an Instagram account. Please ensure you have explicit permission to use this tool on any account.


## Disclaimer

This script is provided for educational and ethical purposes only. Misuse of this script for unauthorized access to Instagram accounts is illegal and unethical. By using this script, you agree that, I (M.Hammad Haider) am not responsible for any illegal or unauthorized use. Use this tool responsibly and only on accounts for which you have explicit permission.

## Features

- Brute force attack on Instagram accounts.
- Custom wordlist creator.
- Session saving for resuming an interrupted attack.
- Multi-threading support for faster password cracking.
- Utilizes Tor for anonymous and secure connections.

## **Note:** 
- Instagram has enhanced its security for repeated incorrect brute forced password attempts.
- That's we I recommend to use proxies or tor for change in IP throughout the attack.


## Prerequisites

Before you begin, make sure you have the following prerequisites:

1. **Tor**: Install Tor for anonymous web browsing and secure connections.
   ```
   sudo apt-get install tor
   ```

## Installation

Follow these steps to install and use BF:

1. **Clone the Repository**: Clone the Insta-Cypher repository from GitHub to your local machine.
   ```
   git clone https://github.com/amfinethankyou/Insta_bruteforce
   ```

2. **Start Tor**: Run the Tor service in another terminal to ensure anonymous and secure connections.
   ```
   tor
   ```

3. **Navigate to the Script Directory**: Change the current directory to the Insta-Cypher directory.
   ```
   cd Insta_bruteforce
   ```

4. **Set Permissions**: Make the script executable by changing its permissions.
   ```
   chmod +x insta.sh
   ```

## Password Lists

- The `default-passwords.lst` included in this repository contains 308,600+ passwords that can be used for brute forcing.
- You can find additional password lists for your brute-force attacks on this GitHub repository: [More Passwords](https://github.com/scipag/password-list)

## Usage

After installation, you can run BF using the following command:
```
python3 bf.py
```

This command will start the script, allowing you to perform brute-force attacks on Instagram accounts.

