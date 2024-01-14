import string
def remove_duplicates(sequence):
    seen = set()
    result = []
    
    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result

def word_frequency(sentence):
    words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency