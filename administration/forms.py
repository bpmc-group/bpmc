from django import forms
from api.models import AccessProfile, Permission


class AccessProfileForm(forms.ModelForm):
    class Meta:
        model = AccessProfile
        fields = ['name', 'description', 'default']


class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['function_name', 'can_view']  # Only include fields present in the updated model


# Formset for creating/editing multiple permissions at once
PermissionFormSet = forms.modelformset_factory(
    Permission,
    form=PermissionForm,
    extra=5  # Number of extra empty forms for new permissions
)
