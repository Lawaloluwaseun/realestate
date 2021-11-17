# Generated by Django 3.2.9 on 2021-11-16 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.agent'),
        ),
    ]