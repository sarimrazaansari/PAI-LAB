# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 10

sentence = input("Enter a sentence: ").lower()
words = sentence.split()
vowels = set("aeiou")

result = {
    word: {
        "vowels": sum(1 for character in word if character in vowels),
        "consonants": sum(1 for character in word if character.isalpha() and character not in vowels)
    }
    for word in words
}

for word, counts in result.items():
    print(word, "-> vowels:", counts["vowels"], "consonants:", counts["consonants"])
