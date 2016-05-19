from django import template

from sliach_rating.models import State, Sluchim


register = template.Library()

@register.inclusion_tag('sliach_rating/state_nav.html')
def nav_state_list():
    '''Returns dictionary of states to display as navigation pane'''
    states = State.objects.all()[:20]
    return {'states': states}
