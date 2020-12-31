def initials(phrase):
    words = phrase
    result = ""
    for word in words.upper().split():
        result += word[0]
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# def initials(phrase):
#     words = phrase.upper().split()
#     result = ""
#     for word in words:
#         result += word
#     return words[0]

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

