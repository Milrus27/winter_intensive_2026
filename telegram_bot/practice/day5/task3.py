import json

my_settings = {
    'name': 'Milrus',
    'status': 'student',
    'goals': ['Python', 'English', 'bot'],
    'weeks_left': 3,
    'date': '2026-01-09'
}

with open('my_file.json', 'w') as f:
    json.dump(my_settings, f, indent=4, ensure_ascii=False)

with open('my_file.json', 'r') as f:
    loaded_file = json.load(f)

print(my_settings, '\n')
print(loaded_file, '\n')
print(my_settings == loaded_file)