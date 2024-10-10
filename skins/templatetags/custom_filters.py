from django import template

register = template.Library()

@register.filter
def format_price_in_euro(value):
    try:
        euro_value = value / 1000
        return f"{euro_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value 
