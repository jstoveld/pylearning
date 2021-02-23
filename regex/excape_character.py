import re

print(re.search(r".com", "welcome"))
## <re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com", "welcome"))
## None

print(re.search(r"\.com", "mydomain.com"))
## <re.Match object; span=(8, 12), match='.com'>

print(re.search(r"\w*", "This is an example"))
## <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "This_is_another_example"))
## <re.Match object; span=(0, 23), match='This_is_another_example'>

