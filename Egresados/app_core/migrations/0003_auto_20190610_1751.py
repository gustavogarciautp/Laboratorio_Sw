# Generated by Django 2.2 on 2019-06-10 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0002_user_is_superuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
