def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("sasuage"))
print(count_letters("psouirfdg09usprfio9jkhgpoiedjkfh"))