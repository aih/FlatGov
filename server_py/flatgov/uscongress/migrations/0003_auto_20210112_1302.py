# Generated by Django 3.1 on 2021-01-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uscongress', '0002_auto_20210112_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uscongressupdatejob',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('success', 'success'), ('failed', 'failed')], default='pending', max_length=20),
        ),
    ]