import json

def load_config(filename='my_file.json'):

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f'The file {filename} was uploaded successfully')
            return data
    
    except FileNotFoundError:
        print(f'The file {filename} not found. Creating a file with default settings')
        default_settings = {
        'name': 'Milrus',
        'status': 'student',
        'goals': ['Python', 'English', 'bot'],
        'weeks_left': 3,
        'date': '2026-01-09'
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(default_settings, f, indent=4, ensure_ascii=False)
        print(f'Created a file with default settings')
        return default_settings
    
    except json.JSONDecodeError:
        print(f'JSON format error in file {filename}')
        return {}
    
    except:
        print(f'Unknown error in file {filename}')
        return {}
    
if __name__ == '__main__':
    print('Configuration test')
    config = load_config() 
    if config:
        for key, value in config.items():
            print(f'{key}: {value}')
    else:
        print('Configuration is empty')