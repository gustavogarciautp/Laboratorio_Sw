# Generated by Django 2.2 on 2019-06-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0009_auto_20190611_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contraseña',
        ),
        migrations.AlterField(
            model_name='superuser',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='Password'),
        ),
    ]
