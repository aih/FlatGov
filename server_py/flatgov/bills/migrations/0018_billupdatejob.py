# Generated by Django 3.1 on 2021-01-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0017_bill_es_similarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillUpdateJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('success', 'success')], default='pending', max_length=20)),
                ('content', models.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
