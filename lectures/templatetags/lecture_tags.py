from django import template

register = template.Library()

@register.filter
def truncate_around(text, keyword):
    index = text.lower().find(keyword.lower())
    if index != -1:
        start_index = max(0, index - 700)
        end_index = min(index + 700, len(text))
        truncated_text = text[start_index:end_index]
        if start_index > 0:
            truncated_text = '...' + truncated_text
        if end_index < len(text):
            truncated_text += '...'
        highlighted_text = f'<strong style="background-color: #00f0ff;">{keyword}</strong>'
        truncated_text = truncated_text.replace(keyword, highlighted_text)
        return truncated_text
    else:
        return text
