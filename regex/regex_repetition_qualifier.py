import re

print(re.search(r"Py.*n", "Pygmalion"))
## <re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py.*n", "Python Programming"))
## <re.Match object; span=(0, 17), match='Python Programmin'>
## Greedy Qualifiers - To not have this use a character class

print(re.search(r"Py[a-z]*n", "Python Programming"))
## <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))
## <re.Match object; span=(0, 3), match='Pyn'>

print(re.search(r"o+l+", "goldfish"))
## <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly"))
## <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))
## None