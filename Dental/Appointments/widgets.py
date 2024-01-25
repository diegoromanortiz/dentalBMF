from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'