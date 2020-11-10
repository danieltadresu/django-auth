from django.contrib import admin

# Register your models here.

from polls.models import Client

admin.site.register(Client)
