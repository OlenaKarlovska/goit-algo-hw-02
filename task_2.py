from collections import deque

def palindrome(text: str) -> bool:
    cleaned_text = "".join(ch.lower() for ch in text if ch.isalnum())
    d = deque(cleaned_text)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
examples = [
    "word",
    "ana",
    "Python",
    "pop"]
for word in examples:
    print(f"'{word}' -> {palindrome(word)}")