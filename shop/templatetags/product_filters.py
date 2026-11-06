from django import template

register = template.Library()


@register.filter
def price_comma(value):
    """
    Format a price with thousand separators, e.g. 120000000 -> 120,000,000.
    Separators are added only when the number has more than 3 digits.
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value

    if abs(value) < 1000:
        return str(value)

    return f"{value:,}"
