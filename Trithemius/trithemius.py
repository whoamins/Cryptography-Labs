import string


alphabet = string.ascii_lowercase
message = "some"
result = str()

for index, char in enumerate(message):
    char_index_in_alphabet = alphabet.index(char)
    a = alphabet[char_index_in_alphabet]

    result += alphabet[char_index_in_alphabet + index + 1]

    alphabet = alphabet[1:] + alphabet[:1]

print(result)
