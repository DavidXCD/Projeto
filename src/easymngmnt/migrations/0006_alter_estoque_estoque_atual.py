# Generated by Django 3.2.9 on 2021-11-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymngmnt', '0005_rename_fornecedpr_estoque_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='estoque_atual',
            field=models.IntegerField(default='0', null=True),
        ),
    ]