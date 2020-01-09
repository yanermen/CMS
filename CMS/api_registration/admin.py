from django.contrib import admin

from .models import PersonData


class PersonDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'password')


admin.site.register(PersonData, PersonDataAdmin)