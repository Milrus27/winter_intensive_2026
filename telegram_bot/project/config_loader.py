import json

def load_config(filename='config.json', template_filename='config_template.json'):

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f'The file {filename} was uploaded successfully')
            return data
    
    except FileNotFoundError:
        print(f'The file {filename} not found. Trying to use the template')
        try:
            with open(template_filename, 'r', encoding='utf-8') as f1:
                data_template = json.load(f1)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data_template, f, indent=4, ensure_ascii=False)
            
            print(f'The template successfully used')
            return data_template
        
        except FileNotFoundError:
            print(f'The template {template_filename} not found. Creating the default config')
            default_config = {
                "bot_token": "YOUR_BOT_TOKEN_HERE",
                "admin_ids": [123456789],
                "reminder_settings": {
                "min_interval_hours": 1,
                "max_per_user": 5,
                "max_text_length": 1000
                },
                "log_level": "INFO"
            }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4, ensure_ascii=False)
        print(f'Created a config with default settings')
        return default_config
    
    except json.JSONDecodeError:
        print(f'JSON format error in file {filename}')
        return {}
    
    except Exception as e:
        print(f'Unknown error in file {filename}. \nError: {e}')
        return {}
    
if __name__ == '__main__':
    print('Configuration test')
    config = load_config()
    if config.get('bot_token') == "YOUR_BOT_TOKEN_HERE":
        print('WARNING: token is not loaded. Install it')
    print('\nToken content:')
    if config:
        for key, value in config.items():
            print(f'{key}: {value}')
    else:
        print('Configuration is empty')
    print('The test is completed')