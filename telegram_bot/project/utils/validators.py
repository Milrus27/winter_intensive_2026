def valid_len_text(text, max_len=1000):
    return len(text) <= max_len

def no_binary(text):
    special = {'\n', '\r', '\t'}
    for char in text:
        if ord(char) < 32 and char not in special:
            return False
    return True