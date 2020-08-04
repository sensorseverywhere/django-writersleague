from django import template
register = template.Library()

@register.filter(name = 'calc_price')
def calc_price( value, arg ):
    '''
    Multiplies the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return value * arg
    except: pass
    return ''