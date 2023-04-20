from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

from .forms import UpdateEmployeePermissionForm, AddNewHappyHourPackage, EventRegistrationForm, ChooseGiftForm, RegistrationForm
from .models import Employee, InvitedGifts


def update_employee_perm(request):
    resp = ''
    form = UpdateEmployeePermissionForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            employee = Employee.objects.get(id=form.cleaned_data['name'].id)
            employee.permission = form.cleaned_data['permission']
            employee.save()
            resp = "Success!"

    return render(
        request,
        "form.html",
        {
            "form": form,
            "resp": resp
        },
    )


def add_new_happy_hour_package(request):
    resp = ''
    form = AddNewHappyHourPackage(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            resp = "Success!"

    return render(
        request,
        "form.html",
        {
            "form": form,
            "resp": resp
        },
    )


def register_to_event(request):
    resp = ''
    form = EventRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            resp = "Success!"

    return render(
        request,
        "form.html",
        {
            "form": form,
            "resp": resp
        },
    )


def choose_holiday_gift(request):
    return choose_gift(0, request)


def choose_birthday_gift(request):
    return choose_gift(1, request)


def choose_gift(type, request):
    print(request.user)
    resp = ''
    form = ChooseGiftForm(type, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            """
            invited_gift = InvitedGifts()
            invited_gift.employee = Employee.objects.get(id=form.cleaned_data['user_id'])
            print(form.cleaned_data.keys())
            invited_gift.gift = form.cleaned_data['id']
            invited_gift.save()
            """

            resp = "Success!"

    return render(
        request,
        "form.html",
        {
            "form": form,
            "resp": resp
        },
    )


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('choose_holiday_gift')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
