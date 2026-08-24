def count_the_len(text):
    words = text.split()
    print(f"Number of words: {len(words)}")
    letters = text.replace(" ", "").replace("\n", "")
    print(f"Number of letters: {len(letters)}")