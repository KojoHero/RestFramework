# Generated by Django 3.1.5 on 2021-01-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_registration_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
