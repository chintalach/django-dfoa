from django.contrib import admin

# Register your models here.
from .models import owner_det,tenant_det

admin.site.register(owner_det)
admin.site.register(tenant_det)