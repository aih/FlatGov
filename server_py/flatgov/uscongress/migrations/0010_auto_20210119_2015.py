# Generated by Django 3.1 on 2021-01-19 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uscongress', '0009_auto_20210114_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uscongressupdatejob',
            old_name='similarity',
            new_name='similarity_status',
        ),
    ]