def safe_logger(text, max_len=200):
    if len(text) > max_len:
        return text[:max_len] + '...'
    return text