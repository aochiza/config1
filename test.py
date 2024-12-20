import sys
import toml
import unittest

file=open("employee.toml","w")
data_dict={
    "employee": {
        "name": "John Doe",
        "age": 35
    },
    "job": {
        "title": "Software Engineer",
        "department": "IT",
        "years_of_experience": 10
    },
    "address": {
        "street": "123 Main St.",
        "city": "San Francisco",
        "state": "CA",
        "zip": 94102
    },
    "game configuration": {
        "resolution_width": 1920,
        "resolution_heightk": 1080,
        "fullscreen": "true",
        "music_volume": 0.5,
        "characters": "player, enemy, npd"
    },
    "web-site configuration": {
        "port": 1920,
        "timeout": 30
    }
}
toml.dump(data_dict,file)
file.close()

data=toml.load("employee.toml")
print("The data from toml file is:")
print(data)


def parse_toml(input_text):
    """Парсит текст TOML и возвращает в виде словаря."""
    try:
        return toml.loads(input_text)
    except toml.TomlDecodeError as e:
        print(f"Ошибка парсинга TOML: {e}", file=sys.stderr)
        sys.exit(1)

def convert_to_custom_language(data):
    """Преобразует словарь из TOML в учебный конфигурационный язык."""
    result = []
    for key, value in data.items():
        if isinstance(value, list):
            result.append(f"{key} = ({', '.join(map(str, value))})")
        elif isinstance(value, dict):
            dict_repr = ', '.join(f"{k} = {v}" for k, v in value.items())
            result.append(f"{key} = dict({dict_repr})")
        elif isinstance(value, str):
            result.append(f"{key} = [[{value}]]")
        else:
            result.append(f"{key} = {value}")

    return '\n'.join(result)

def main():
    """Основная функция, считывающая входные данные и выводящая результат."""
    input_text = sys.stdin.read()
    data = parse_toml(input_text)
    output = convert_to_custom_language(data)
    print(output)

class TestTomlToCustomLanguage(unittest.TestCase):
    def test_flat_structure(self):
        toml_input = """
        title = "Тестовая конфигурация"
        version = 1.0
        """
        expected_output = "title = [[Тестовая конфигурация]]\nversion = 1.0"
        data = parse_toml(toml_input)
        output = convert_to_custom_language(data)
        self.assertEqual(output, expected_output)

    def test_array_structure(self):
        toml_input = """
        authors = ["Alice", "Bob", "Charlie"]
        """
        expected_output = "authors = (Alice, Bob, Charlie)"
        data = parse_toml(toml_input)
        output = convert_to_custom_language(data)
        self.assertEqual(output, expected_output)

    def test_dictionary_structure(self):
        toml_input = """
        database = {host = "localhost", port = 5432}
        """
        expected_output = "database = dict(host = [[localhost]], port = 5432)"
        data = parse_toml(toml_input)
        output = convert_to_custom_language(data)
        self.assertEqual(output, expected_output)

    def test_nested_structure(self):
        toml_input = """
        server = {host = "127.0.0.1", port = 8080}
        database = {user = "user", password = "password", server = {host = "localhost", port = 5432}}
        """
        expected_output = (
            "server = dict(host = [[127.0.0.1]], port = 8080)\n"
            "database = dict(user = [[user]], password = [[password]], server = dict(host = [[localhost]], port = 5432))"
        )
        data = parse_toml(toml_input)
        output = convert_to_custom_language(data)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main()
    else:
        main()