stop_words = {
    "a", "an", "the",
    "and", "or", "but",
    "if", "then", "else",
    "for", "while", "do",
    "of", "in", "on", "at", "to", "from", "by", "with",
    "is", "am", "are", "was", "were", "be", "been", "being",
    "has", "have", "had",
    "can", "could", "will", "would", "shall", "should", "may", "might", "must",
    "i", "me", "my", "mine",
    "you", "your", "yours",
    "he", "him", "his",
    "she", "her", "hers",
    "it", "its",
    "we", "us", "our", "ours",
    "they", "them", "their", "theirs",
    "this", "that", "these", "those",
    "who", "whom", "which", "what", "when", "where", "why", "how",
    "not", "no", "nor",
    "as", "than", "too", "very",
    "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
    "only", "own", "same", "so", "just"
}

def keyword_extraction(text):
    words = text.split()
    dict_words = {}
    for word in words:
        if word not in stop_words:
            dict_words[word] = dict_words.get(word, 0) + 1
    sorted_words = sorted(dict_words.items(), key=lambda item: item[1], reverse=True)
    return sorted_words