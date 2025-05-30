import itertools

def brute_force_passwords(charset, min_length, max_length):
    """
    Generator that yields all possible password combinations
    using the given charset and length range.
    """
    for length in range(min_length, max_length + 1):
         # itertools.product returns tuples of characters
        for pw_tuple in itertools.product(charset, repeat=length):
            # Join tuple into a string
            yield ''.join(pw_tuple)