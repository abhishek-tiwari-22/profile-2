# Generated by Django 3.1.7 on 2021-07-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210711_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='dob',
            field=models.DateField(),
        ),
    ]
