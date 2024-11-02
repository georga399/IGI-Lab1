import calendar
import datetime

from django import template

register = template.Library()


@register.filter
def my_calendar(text):
    return str(calendar.HTMLCalendar().formatmonth(datetime.datetime.now().year, datetime.datetime.now().month))