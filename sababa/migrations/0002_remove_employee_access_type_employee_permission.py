# Generated by Django 4.1.7 on 2023-03-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sababa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='access_type',
        ),
        migrations.AddField(
            model_name='employee',
            name='permission',
            field=models.CharField(choices=[('WR', 'Worker'), ('TL', 'Team Leader'), ('DM', 'Direct Manager'), ('HR', 'Hr'), ('FN', 'Finance'), ('SU', 'Superuser')], default='WR', max_length=2),
        ),
    ]
