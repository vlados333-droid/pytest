import json

# === Часть 1: Запись данных в JSON-файл ===
def write_to_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Данные записаны в файл {filename}.")


# === Часть 2: Чтение данных из JSON-файла ===
def read_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(f"Данные из файла {filename}:")
    print(json.dumps(data, indent=4, ensure_ascii=False))  # Красивый вывод
    return data


# === Часть 3: Работа с JSON-строкой ===
def process_json_string():
    json_string = '''
    {
        "name": "Иван",
        "age": 25,
        "hobbies": ["Чтение", "Программирование", "Путешествия"],
        "is_active": true,
        "address": {
            "city": "Москва",
            "zip_code": "123456"
        }
    }
    '''
    # Преобразование JSON-строки в Python-объект
    python_object = json.loads(json_string)
    print("Python объект из JSON строки:")
    print(python_object)

    # Преобразование Python-объекта обратно в JSON-строку
    new_json_string = json.dumps(python_object, indent=4, ensure_ascii=False)
    print("JSON строка из Python объекта:")
    print(new_json_string)


# === Часть 4: Основной код ===
if __name__ == "__main__":
    # Пример данных
    example_data = {
        "users": [
            {"id": 1, "name": "Иван", "age": 25},
            {"id": 2, "name": "Анна", "age": 30},
            {"id": 3, "name": "Петр", "age": 35}
        ],
        "active": True,
        "total_users": 3
    }

    # Имя JSON-файла
    file_name = "example.json"

    # Запись данных в файл
    write_to_json_file(file_name, example_data)

    # Чтение данных из файла
    read_data = read_from_json_file(file_name)

    # Работа с JSON-строкой
    process_json_string()
