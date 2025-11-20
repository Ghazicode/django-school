from django import template

register = template.Library()

@register.filter
def truncate_chars(text, num_chars=30):
    if not text:
        return ""
    
    text = str(text)
    if len(text) <= num_chars:
        return text
    
    return text[:num_chars] + "..."




@register.filter
def first_letters(text):
    if not text:
        return ""
    
    text = str(text)
    # گرفتن اولین حرف هر کلمه
    words = text.split()
    first_chars = [word[0] for word in words if word]
    
    return ''.join(first_chars)