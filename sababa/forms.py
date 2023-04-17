from django import forms
from django.forms.widgets import Select

from .models import Employee, HappyHour, EventRegistration, Gifts, InvitedGifts


class UpdateEmployeePermissionForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("name", "permission", )

    def __init__(self, *args, **kwargs):
        super(UpdateEmployeePermissionForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ModelChoiceField(
            queryset=Employee.objects.all(),
            to_field_name="id")


class AddNewHappyHourPackage(forms.ModelForm):
    class Meta:
        model = HappyHour
        fields = '__all__'


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = '__all__'


class ChooseGiftForm(forms.ModelForm):
    class Meta:
        model = InvitedGifts
        fields = '__all__'

    def __init__(self, type, *args, **kwargs):
        super(ChooseGiftForm, self).__init__(*args, **kwargs)
        self.fields['employee'] = forms.ModelChoiceField(
            queryset=Employee.objects.all(),
            to_field_name="id")

        # TODO: Select type to be specific
        self.fields['gift'] = forms.ModelChoiceField(
            queryset=Gifts.objects.all(),
            to_field_name="id")
