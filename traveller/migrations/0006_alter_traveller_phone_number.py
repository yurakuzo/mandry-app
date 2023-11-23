# Generated by Django 4.2.5 on 2023-10-05 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveller', '0005_remove_traveller_rating_alter_traveller_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveller',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(12)]),
        ),
    ]
