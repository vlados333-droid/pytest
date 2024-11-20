import json


def write_to_json_file(filename, data):
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f'Данные записаны в файл {filename}')


def read_from_json_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)
    print(f'Данные из файла {filename}: ')
    print(json.dumps(data, indent=4, ensure_ascii=False))
    return data


def process_json_string():
    json_str = '''
    {
        "name": "Иван",
        "age": 25,
        "hobbies": ["Чтение", "Шахматы", "Программирование"],
        "is_active": true,
        "address": {
            "city": "Москва",
            "zip_code": "123456"
        }
    }
    '''

    python_object = json.loads(json_str)
    print('Python объект из JSON строки: ')
    print(python_object)

    new_python_str = json.dumps(python_object, indent=4, ensure_ascii=False)
    print('JSON строка из Python объекта: ')
    print(new_python_str)


if __name__ == "__main__":
    file_name = 'example.json'

    example_data = {
        "users": [
            {"id": 1, "name": 'Иван', "age": 25},
            {"id": 2, "name": 'Анна', "age": 30},
            {"id": 3, "name": 'Петр', "age": 35},
        ],
        "active": True,
        "total_users": 3,
    }

    write_to_json_file(file_name, example_data)

    read_data = read_from_json_file(file_name)
    print("read_data start")
    print(read_data)
    print("read_data end")

    process_json_string()
