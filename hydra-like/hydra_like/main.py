import argparse
from brute import brute_force_passwords
from ssh_attack import try_ssh_login
from wordlist import load_wordlist
import time

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Hydra-like tool for password cracking")
    parser.add_argument('-u', '--username', required=True, help="Username for SSH login")
    parser.add_argument('-s','--server', required=True, help="Server IP or DNS name")
    parser.add_argument('-w','--wordlist', help="Path to wordlist file (optional)")
    parser.add_argument('--min', type=int, default=1, help="Minimum length of the password (for brute force)")
    parser.add_argument('--max', type=int, default=20, help="Maximum length of the password (for brute force)")
    parser.add_argument('-c', '--chartset', default='abcdefghijklmnopqrstuvwxyz', help="Chartset for brute force")
    args = parser.parse_args()

    # Choose password source: wordlist or brute force
    if args.wordlist:
        # Load wordlist from file
        password_generator = load_wordlist(args.wordlist)
    else:
        # Generate passwords using brute force
        password_generator = brute_force_passwords(args.chartset, args.min, args.max)
    
    for password in password_generator:
        print(f"Trying password: {password}")
        # Try the password against the SSH server
        if try_ssh_login(args.server, args.username, password):
            print(f"Username: {args.username}")
            print(f"Server: {args.server}")
            print(f"Success! Password found: {password}")
            break
        # Sleep for 0.5 seconds to avoid overwhelming the server
        time.sleep(2)
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
