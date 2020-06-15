"""Search 4 Letters Function"""
# Learn about sets
# arguments with datatypes
# functions that return a value


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in  'phrase'"""
    return set(letters).intersection(set(phrase))


"""
v = search4vowels('hitch-hiker')
print(v)

letters = {'a', 'e', 'i', 'o', 'u'}
print(letters)

letters = {'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'}
print(letters)

letters = set('aeiou')
print(letters)

phrase = set('some random word')
print(phrase)

print(letters.intersection(phrase))

print("-" * 50)
m = search4letters("some random word")
print(m)

m = search4letters("some random word", "power")
print(m)
"""
