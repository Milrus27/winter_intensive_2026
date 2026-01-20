import json
import logging

logger = logging.getLogger(__name__)

def load_config(filename='config.json', template_filename='config_template.json'):

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            #  logger.info(f'The file {filename} was uploaded successfully')
            return data
    
    except FileNotFoundError:
        print(f'The file {filename} not found. Trying to use the template')
        try:
            with open(template_filename, 'r', encoding='utf-8') as f1:
                data_template = json.load(f1)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data_template, f, indent=4, ensure_ascii=False)
            
            logger.info(f'The template successfully used')
            return data_template
        
        except FileNotFoundError:
            logger.warning(f'The template {template_filename} not found. Creating the default config')
            default_config = {
                "bot_token": "YOUR_BOT_TOKEN_HERE",
                "admin_ids": [123456789],
                "reminder_settings": {
                "min_interval_hours": 1,
                "max_per_user": 5,
                "max_text_length": 1000,
                },
                "blacklist": []
            }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4, ensure_ascii=False)
        logger.info(f'Created a config with default settings')
        return default_config
    
    except json.JSONDecodeError:
        logger.error(f'JSON format error in file {filename}')
        return {}
    
    except Exception as e:
        logger.error(f'Unknown error in file {filename}. \nError: {e}')
        return {}