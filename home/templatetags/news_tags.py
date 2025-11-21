from django import template

register = template.Library()

@register.filter
def news_tag(text, num_chars=50):
    if not text:
        return ""
    
    text = str(text)
    if len(text) <= num_chars:
        return text

    return text[:num_chars] + "..."


