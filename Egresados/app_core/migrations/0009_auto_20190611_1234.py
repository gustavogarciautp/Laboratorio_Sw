# Generated by Django 2.2 on 2019-06-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0008_auto_20190611_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contraseña',
            field=models.CharField(default='', max_length=128, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='superuser',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='Contraseña'),
        ),
    ]
