import sys
import toml

file = open("employee.toml", "w")
data_dict = {
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
        "resolution_height": 1080,
        "fullscreen": "true",
        "music_volume": 0.5,
        "characters": "player, enemy, npd"
    },
    "web-site configuration": {
        "port": 1920,
        "timeout": 30
    }
}
toml.dump(data_dict, file)
file.close()

data = toml.load("employee.toml")

def parse_toml(input_text):
    try:
        return toml.loads(input_text)
    except toml.TomlDecodeError as e:
        print(f"Ошибка парсинга TOML: {e}", file=sys.stderr)
        sys.exit(1)

def convert_to_custom_language(data):
    result = ["set v1 = 1920;"]
    result.append("dict(")

    for key, value in data.items():
        dict_repr = ', '.join(
            f"{k} = {('|v1|' if v == 1920 else v)}" if isinstance(v, int) else f"{k} = {v}"
            for k, v in value.items()
        )
        result.append(f"{key} = dict({dict_repr}),")

    result.append(")")
    return '\n'.join(result)

def main():
    input_text = sys.stdin.read()
    data = parse_toml(input_text)
    output = convert_to_custom_language(data)
    print(output)

if __name__ == "__main__":
    main()