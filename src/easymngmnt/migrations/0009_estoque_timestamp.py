# Generated by Django 3.2.9 on 2021-11-20 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('easymngmnt', '0008_alter_estoque_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]