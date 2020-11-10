from django.forms import ModelForm
from .models import owner_det,tenant_det


class OwnerDetailsForms(ModelForm):
    class Meta:
        model = owner_det
        fields = '__all__'

class TenantDetailsForms(ModelForm):
    class Meta:
        model = tenant_det
        fields = '__all__'
