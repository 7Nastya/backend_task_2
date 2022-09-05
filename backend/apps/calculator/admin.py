from django.contrib import admin
from .models import Ipoteka


class IpotekaAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'term_min', 'term_max', 'rate_min', 'rate_max', 'payment_min', 'payment_max')


admin.site.register(Ipoteka, IpotekaAdmin)
