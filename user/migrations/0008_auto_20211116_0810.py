# Generated by Django 3.2.9 on 2021-11-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211116_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='password',
            new_name='description',
        ),
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
