def get_string_methods():
    count = 0
    for method in dir(str):
        if not method.startswith('_'):
            count += 1
            print(f"{count}: {method}")

get_string_methods()