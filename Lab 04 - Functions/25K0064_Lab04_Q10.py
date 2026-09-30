def word_frequency(sentence):
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def most_common(counts, n=1):
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:n]

sentence = input("Enter a sentence: ")
counts = word_frequency(sentence)
print(counts)
print(most_common(counts))
print(most_common(counts, 3))