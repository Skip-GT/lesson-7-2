def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(len(strings_positions) + 1, position)] = string
    return strings_positions


file_name = 'test.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.',
           'Because there are 2 languages!',  'Спасибо!']

result = custom_write(file_name, strings)
print(result)