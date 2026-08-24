
from text_analyzer.utils import processor

positive_w = {
    "good", "great", "excellent", "happy", "love", 
    "amazing", "nice", "best", "wonderful", "perfect", 
    "awesome", "beautiful", "success"
}

negative_w = {
    "bad", "terrible", "hate", "worst", "sad", 
    "poor", "awful", "angry", "boring", "problem", 
    "failure", "ugly"
}

def sentiment(text):
    words = processor(text).split()
    pos = 0
    neg = 0
    
    for word in words:
        if word in positive_w:
            pos += 1
        elif word in negative_w:
            neg += 1
            
    total = neg + pos
    if total == 0:
        return "Neutral", 0
        
    rate = (max(pos, neg) / total) * 100
    
    if pos > neg:
        sentiment_res = "Positive"
    elif neg > pos:
        sentiment_res = "Negative"
    else:
        sentiment_res = "Neutral"
    return sentiment_res, rate