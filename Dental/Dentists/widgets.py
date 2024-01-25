from django import forms
from datetime import date  # Agregar esta línea para importar el tipo de dato date

class DateInput(forms.DateInput):
    '''Defines the date input I want.'''
    input_type = 'date'

    def format_value(self, value):
        if isinstance(value, str):
            return value  # Return the date value as it is (YYYY-MM-DD)
        elif isinstance(value, date):
            return value.strftime('%Y-%m-%d')  # Format date as string (YYYY-MM-DD)
        return ''  # Return an empty string for invalid input or None

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        # Aquí puedes anular días en el calendario.
        # Por ejemplo, deshabilitar los fines de semana (sábado y domingo):
        weekends = [5, 6]  # 0 = lunes, 1 = martes, ..., 6 = domingo
        disabled_days = [day for day in weekends if day not in self.get_disabled_days()]

        # Añadir la información al contexto para que sea utilizada por la plantilla.
        context['widget']['attrs']['disabled_days'] = disabled_days
        return context

    def get_disabled_days(self):
        # Aquí debes implementar la lógica para determinar qué días deben ser deshabilitados.
        # Por ejemplo, puedes leer esta información de la base de datos o de algún archivo de configuración.
        # En este ejemplo, simplemente deshabilitaremos el día 25 de cada mes.
        disabled_days = [(2023, 7, 25), (2023, 8, 25)]  # Formato: (año, mes, día)
        return disabled_days
