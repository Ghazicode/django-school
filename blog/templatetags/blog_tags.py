from django import template

register = template.Library()

@register.filter
def truncate_chars(text, num_chars=30):
    if not text:
        return ""
    
    text = str(text)
    if len(text) <= num_chars:
        return text
    
    if num_chars == 1:
        return text[:num_chars] 

    
    return text[:num_chars] + "..."


