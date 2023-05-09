from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User


"""
TODO: 
1. Letting only permitted users to permit (hr perm, etc)
2. birthday view
3. add everything to the design 
4. watching birthdays + sending birthday messages via mail
5. Bug fixes :))
"""


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


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = '__all__'


class ChooseGiftForm(forms.ModelForm):
    class Meta:
        model = OrderedGifts
        fields = '__all__'

    def __init__(self, type, *args, **kwargs):
        super(ChooseGiftForm, self).__init__(*args, **kwargs)
        self.fields['employee'] = forms.ModelChoiceField(
            queryset=Employee.objects.all(),
            to_field_name="id")

        self.fields['gift'] = forms.ModelChoiceField(
            queryset=Gifts.objects.get(type=type),
            to_field_name="id")


class RegistrationForm(UserCreationForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), to_field_name="id")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'employee')

    def save(self, commit=True):
        user = super().save(commit=False)
        user_profile = UserProfile(user=user, employee=self.cleaned_data['employee'])
        if commit:
            user.save()
            user_profile.save()
        return user, user_profile


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class WelfareActivityRequestForm(forms.ModelForm):
    class Meta:
        model = WelfareActivity
        fields = '__all__'
