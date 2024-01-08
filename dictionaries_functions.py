import string

def word_frequency(sentence):
    words = sentence.lower().split()
    cleaned_words = [word.strip(string.punctuation) for word in words]
    
    frequency = {}
    for word in cleaned_words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
