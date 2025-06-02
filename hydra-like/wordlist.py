def load_wordlist(file_path):
    """
    Loads a wordlist from a file and returns a list of passwords.
    """
    # Generator function that yields passwords one by one
    try:
        # Open the file and read it line by line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                password = line.strip()
                if password: # Skip empty lines
                    yield password
    except FileNotFoundError:
        print(f"Wordlist file not found: {file_path}")
        return