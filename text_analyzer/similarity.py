from text_analyzer.utils import processor

def text_similarity(text1, text2):
    text1 = processor(text1)
    text2 = processor(text2)

    text1 = set(text1.split())
    text2 = set(text2.split())

    most = text1 & text2
    all_w = text1 | text2

    if len(all_w) == 0:
        print("No words entered")
        return 0

    similarity = (len(most) / len(all_w)) * 100
    return similarity