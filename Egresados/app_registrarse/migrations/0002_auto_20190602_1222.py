# Generated by Django 2.2 on 2019-06-02 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_registrarse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrarse',
            old_name='nombres',
            new_name='nombre',
        ),
    ]
