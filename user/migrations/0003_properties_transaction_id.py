# Generated by Django 3.2.9 on 2021-11-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_properties_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='transaction_id',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
