# Generated by Django 3.2.9 on 2021-11-19 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easymngmnt', '0004_auto_20211119_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='fornecedpr',
            new_name='fornecedor',
        ),
    ]