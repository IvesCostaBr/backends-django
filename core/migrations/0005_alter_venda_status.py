# Generated by Django 3.2.2 on 2021-05-10 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210510_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='status',
            field=models.CharField(default='em processo', max_length=20),
        ),
    ]
