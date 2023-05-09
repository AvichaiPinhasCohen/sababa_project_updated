from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import connections
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


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


def add_event(request):
    resp = ''
    form = AddEventForm(request.POST or None)
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
    return choose_gift(Gifts.Type.HOLIDAY, request)


def choose_birthday_gift(request):
    return choose_gift(Gifts.Type.BIRTHDAY, request)


@login_required
def choose_gift(type, request):
    resp = ''
    form = ChooseGiftForm(type, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ordered_gift = OrderedGifts()
            ordered_gift.employee = (UserProfile.objects.get(user=User.objects.get(id=request.user.id))).employee
            ordered_gift.gift = form.cleaned_data['id']
            ordered_gift.save()

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


def add_employee_view(request):
    resp = ''
    form = AddEmployeeForm(request.POST or None)
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


def add_welfare_activity_request_view(request):
    resp = ''
    form = WelfareActivityRequestForm(request.POST or None)
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


def add_preferred_benefits_view(request):
    resp = ''
    records = Benefits.objects.all()
    return render(request, 'list_records.html', {'url': 'edit_benefits_view', 'resp': resp, 'records': records})


@login_required
def edit_benefits_view(request, pk):
    resp = 'Failed'
    record = get_object_or_404(Benefits, pk=pk)
    ChosenBenefits.objects.create(benefit=record, employee=(UserProfile.objects.get(user=User.objects.get(id=request.user.id))).employee)
    resp = 'Added successfully'
    # Render a template with the record's data and an edit form
    print(pk)
    return render(request, 'list_records.html', {'url': 'edit_benefits_view', 'resp': resp, 'record': record})


def welfare_activity_confirmation_view(request):
    resp = ''
    records = WelfareActivity.objects.all()
    return render(request, 'list_records.html', {'url': 'edit_welfare_activity_confirmation_view', 'resp': resp, 'records': records})


def edit_welfare_activity_confirmation_view(request, pk):
    resp = 'Failed'
    # TODO: Get employee id and type, update confirm by type. also add another button - accept and faliure
    record = get_object_or_404(WelfareActivity, pk=pk)
    # TODO: Update welfare activity
    resp = 'Updated successfully'
    # Render a template with the record's data and an edit form
    print(pk)
    return render(request, 'list_records.html', {'resp': resp, 'record': record})


def welfare_acitivity_index_view(request):
    welfare_activities = WelfareActivity.objects.all().values()
    template = loader.get_template('welfare_activities.html')
    context = {
        'welfare_activities': welfare_activities
    }
    return HttpResponse(template.render(context, request))


def welfare_activity_update_view(request, id):
    activity = WelfareActivity.objects.get(id=id)
    template = loader.get_template('welfare_activity_update.html')
    context = {
        'activity': activity,
    }
    return HttpResponse(template.render(context, request))


def welfare_activity_updaterecord_view(request, id):
    activity = WelfareActivity.objects.get(id=id)
    if request.POST.get('submit_button') == 'hr':
        activity.hr_perm = True
    elif request.POST.get('submit_button') == 'finance':
        activity.finance_perm = True
    elif request.POST.get('submit_button') == 'dm':
        activity.manager_perm = True
    elif request.POST.get('dis_submit_button') == 'hr_dis':
        activity.hr_perm = False
        activity.reason = request.POST['reason']
    elif request.POST.get('dis_submit_button') == 'finance_dis':
        activity.finance_perm = False
        activity.reason = request.POST['reason']
    elif request.POST.get('dis_submit_button') == 'dm_dis':
        activity.manager_perm = False
        activity.reason = request.POST['reason']
    else:
        activity.name = request.POST['name']
        activity.max_participants = request.POST['max_participants']
        activity.dates = request.POST['dates']
        activity.contact = request.POST['contact']
        activity.description = request.POST['description']

    activity.save()
    return HttpResponseRedirect(reverse('welfare_acitivity_index'))


def table_list_view(request):
    table_info = {}
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]
            table_info[table_name] = column_names
    return render(request, 'table_list.html', {'table_info': table_info})


def display_table_view(request):
    tables = []
    for key in request.GET.keys():
        if '[]' in key:
            tables.append(key)

    columns = {}
    for table in tables:
        column_list = request.GET.getlist(table)
        if len(column_list) > 0:
            columns[table] = column_list
    data = {}

    with connections['default'].cursor() as cursor:
        for table, column_list in columns.items():
            cursor.execute(f"SELECT {','.join(column_list)} FROM {table[:-2]}")
            rows = cursor.fetchall()
            data[table[:-2]] = rows
    return render(request, 'display_table.html', {'data': data})
