from django import forms
from django.utils.safestring import mark_safe


class CalendarWidget(forms.DateInput):
    class Media:
        css = {
            'all': (
                'http://code.jquery.com/ui/1.10.4/themes/ui-dar\
                kness/jquery-ui.css',)
        }
        js = ('http://code.jquery.com/jquery-1.7.2.min.js',
              'http://code.jquery.com/ui/1.10.2/jquery-ui.js',)

    def __init__(self, params='', attrs=None):
        self.params = params
        super(CalendarWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(CalendarWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').datepicker({%s});
            </script>''' % (name, self.params,))
