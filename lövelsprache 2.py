diphthong_dict = {
    'au': 'alewau',
    'ie': 'ilewie',
    'ei': 'elewei'
}

def translate_to_spoon_language(input_string):
    output_string = ''
    i = 0
    while i < len(input_string):
        found = False
        for diphthong, translation in diphthong_dict.items():
            if input_string[i:i+len(diphthong)] == diphthong:
                output_string += translation
                i += len(diphthong)
                found = True
                break
        if not found:
            output_string += translation_dict.get(input_string[i], input_string[i])
            i += 1
    return output_string

input_string = 'Haus'
output_string = translate_to_spoon_language(input_string)
print(output_string)
