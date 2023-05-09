from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.CharField(max_length=100, default="No description added")


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Permission(models.TextChoices):
        WORKER = 'WR'
        TEAM_LEADER = 'TL'
        DIRECT_MANAGER = 'DM'
        HR = 'HR'
        FINANCE = 'FN'
        SUPERUSER = 'SU'

    permission = models.CharField(
        max_length=2,
        choices=Permission.choices,
        default=Permission.WORKER,
    )

    def __str__(self):
        return self.name


class EventRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Events, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()


class Benefits(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    added_date = models.DateField()


class ChosenBenefits(models.Model):
    benefit = models.ForeignKey(Benefits, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class Gifts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Type(models.TextChoices):
        BIRTHDAY = 'BIRTHDAY'
        HOLIDAY = 'HOLIDAY'

    type = models.CharField(
        max_length=8,
        choices=Type.choices,
    )

    def __str__(self):
        return self.name


class OrderedGifts(models.Model):
    order_id = models.AutoField(primary_key=True)
    gift = models.ForeignKey(Gifts, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class HappyHour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    supplier = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)


class WelfareActivity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    max_participants = models.IntegerField()
    date = models.DateField(default=date(1970, 1, 1))
    contact = models.CharField(max_length=100)
    description = models.CharField(max_length=256, default="No description added")
    reason = models.CharField(max_length=256, default="No reason added")
    manager_perm = models.BooleanField(default=False)
    hr_perm = models.BooleanField(default=False)
    finance_perm = models.BooleanField(default=False)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    orderer = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True)
    welfare_order = models.ForeignKey(WelfareActivity, on_delete=models.DO_NOTHING, null=True)
    happy_hour_order = models.ForeignKey(
        WelfareActivity, on_delete=models.DO_NOTHING, null=True, related_name='happy_hour')
    order_date = models.DateField(max_length=20)
    asked_date = models.DateField(max_length=20)
    manager_perm = models.BooleanField()
    hr_perm = models.BooleanField()
    finance_perm = models.BooleanField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True)
