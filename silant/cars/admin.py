from django.contrib import admin

from .models import Machine, Maintenance, Claim


admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Claim)
