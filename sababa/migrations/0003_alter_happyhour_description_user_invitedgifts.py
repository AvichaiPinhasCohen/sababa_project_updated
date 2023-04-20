# Generated by Django 4.1.7 on 2023-04-20 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sababa', '0002_remove_employee_access_type_employee_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happyhour',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sababa.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvitedGifts',
            fields=[
                ('invitation_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sababa.employee')),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sababa.gifts')),
            ],
        ),
    ]