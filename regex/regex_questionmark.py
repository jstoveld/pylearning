import re

print(re.search(r"p?each", "To each their own"))
## <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like peaches"))
##<re.Match object; span=(7, 12), match='peach'>