import re

print(re.search(r"A.*a", "Argentina"))
## <re.Match object; span=(0, 9), match='Argentina'>

print(re.search(r"A.*a", "Azerbaijan"))
## <re.Match object; span=(0, 9), match='Azerbaija'>
## Note that this is not getting all of the content - we need a stricter pattern


print(re.search(r"^A.*a$", "Azerbaijan"))
## None


print(re.search(r"^A.*a$", "Australia"))
## <re.Match object; span=(0, 9), match='Australia'>


pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_This_Is_A_valid_variable"))
## <re.Match object; span=(0, 25), match='_This_Is_A_valid_variable'>
print(re.search(pattern, "this is not a valid variable"))
## None

print(re.search(pattern, "my_variable1"))
## <re.Match object; span=(0, 12), match='my_variable1'>

print(re.search(pattern, "2my_variable1"))
## None


