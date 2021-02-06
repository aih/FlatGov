# Generated by Django 3.1 on 2021-01-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0018_billupdatejob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=127)),
                ('bill', models.CharField(max_length=250)),
                ('congress', models.CharField(max_length=10)),
                ('date_issued', models.CharField(max_length=35)),
                ('pdf_link', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
