# Generated by Django 3.2.9 on 2021-11-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymngmnt', '0002_rename_etq_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]