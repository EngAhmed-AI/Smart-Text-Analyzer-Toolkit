def processor(text):
    punctuation_list = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
        ',', '.', '؟', '،', '=', '+', '_', '-', '~', '{', 
        '}', '[', ']', ';', ':', '"', "'", '/', '<', '>', 
        '\\', '|', '?', '`'
    ]
    cleaned_chars = [x for x in text.lower() if x not in punctuation_list]
    return "".join(cleaned_chars)