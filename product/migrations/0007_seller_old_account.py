# Generated by Django 3.2.8 on 2021-10-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_dailyboxoperation_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='old_account',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
