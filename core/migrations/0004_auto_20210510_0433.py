# Generated by Django 3.2.2 on 2021-05-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(default='em processo', max_length=10),
        ),
    ]
