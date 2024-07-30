def slugify(text: str) -> str:
    split_text = text.split("-")
    text = " ".join(split_text)
    return text[0].upper() + text[1:].lower()
