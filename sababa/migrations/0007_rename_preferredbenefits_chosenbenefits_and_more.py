# Generated by Django 4.1.7 on 2023-05-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sababa', '0006_remove_userprofile_phone_number_userprofile_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PreferredBenefits',
            new_name='ChosenBenefits',
        ),
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.CharField(default='No description added', max_length=100),
        ),
        migrations.AddField(
            model_name='welfareactivity',
            name='description',
            field=models.CharField(default='No description added', max_length=256),
        ),
        migrations.AddField(
            model_name='welfareactivity',
            name='finance_perm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='welfareactivity',
            name='hr_perm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='welfareactivity',
            name='manager_perm',
            field=models.BooleanField(default=False),
        ),
    ]
