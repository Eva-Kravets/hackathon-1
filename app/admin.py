from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'number', 'email')
    search_fields = ('name', 'surname')


admin.site.register(Person, PersonAdmin)
