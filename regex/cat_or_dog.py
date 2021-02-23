import re   

print(re.search(r"cat|dog", "I like cats."))## <re.Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I like dogs."))## <re.Match object; span=(7, 10), match='dog'>
print(re.search(r"cat|dog", "I like both dogs and cats."))## <re.Match object; span=(12, 15), match='dog'> Search finds only the first instance and not all
print(re.findall(r"cat|dog", "I like both dogs and cats."))## ['dog', 'cat']
