from django import template

register = template.Library()

@register.simple_tag
def date_munger(date1, date2):
    dates=[date1, date2];
    dates.sort()
    if dates[0].date()==dates[1].date():
        return ''.join([dates[0].strftime('%a %d %b %Y'),' <br/>',dates[0].strftime('%H:%M'),' - ',dates[1].strftime('%H:%M')])
    else:
        return ''.join([dates[0].strftime('%a %d %b %Y %H:%M'), ' - <br/>', dates[1].strftime('%a %d %b %Y %H:%M')])
