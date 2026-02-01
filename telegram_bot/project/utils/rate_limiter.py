import time

def limiter(user_data, interval=1.0):
    current_time = time.time()
    last_time = user_data.get('last_message_time', 0)
    if current_time - last_time < interval:
        return True
    user_data['last_message_time'] = current_time
    return False