# Generated by Django 3.2.9 on 2021-11-20 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymngmnt', '0009_estoque_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='recebido',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]