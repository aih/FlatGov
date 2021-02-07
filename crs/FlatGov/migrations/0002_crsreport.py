# Generated by Django 3.1.6 on 2021-02-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlatGov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrsReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='Report title')),
                ('file', models.TextField(help_text='Report file name')),
                ('date', models.DateField(help_text='Latest pub date of the report')),
                ('metadata', models.JSONField(help_text='Report metadata in JSON form', null=True)),
                ('report_content_raw', models.TextField(help_text='Report raw text extracted from HTML. It does not include report summary, look to metadata for it.', null=True)),
                ('bills', models.ManyToManyField(help_text='Bills associated with this report', to='FlatGov.Bill')),
            ],
            options={
                'db_table': 'crs_report',
            },
        ),
    ]
