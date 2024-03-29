def removeStartWithS(text: str):
    """Remove all words in the text that starts with S."""
    text2 = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    words = text2.split(' ')
    for w in words:
        if w.startswith('s') or w.startswith('S'):
            text = text.replace(w, '')
    return text