def count_vowels(text):
    counts = {vowel: 0 for vowel in "aeiou"}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
    return counts

def count_consonants(text):
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

text = input("Enter a sentence: ")
print(count_vowels(text))
print(count_consonants(text))