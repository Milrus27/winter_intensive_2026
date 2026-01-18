import time

def limiter(user_date, interval=1.0):
    current_time = time.time()
    last_time = user_date.get('last_message_time', 0)
    if current_time - last_time < interval:
        return True
    user_date['last_message_time'] = current_time
    return False