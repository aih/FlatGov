# Generated by Django 3.1.8 on 2021-04-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CboReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=1000)),
                ('original_pdf_link', models.CharField(max_length=255)),
                ('congress', models.CharField(max_length=55)),
                ('bill_number', models.CharField(max_length=127)),
                ('bill_id', models.CharField(blank=True, max_length=127, null=True)),
                ('date_fetched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('bill_number', models.CharField(blank=True, max_length=127, null=True)),
                ('chamber', models.CharField(blank=True, max_length=127, null=True)),
                ('category', models.CharField(max_length=127)),
                ('committee', models.CharField(max_length=500)),
                ('report_number', models.CharField(max_length=500)),
                ('associated_legislation', models.CharField(max_length=500)),
                ('original_pdf_link', models.CharField(max_length=500)),
                ('report_type', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=500)),
                ('congress', models.CharField(blank=True, max_length=127, null=True)),
                ('request_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PressStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=500)),
                ('title', models.TextField()),
                ('statement_type', models.CharField(max_length=500)),
                ('member_id', models.CharField(max_length=500)),
                ('congress', models.CharField(max_length=127)),
                ('member_uri', models.CharField(max_length=1000)),
                ('name', models.CharField(blank=True, max_length=127, null=True)),
                ('chamber', models.CharField(blank=True, max_length=127, null=True)),
                ('state', models.CharField(blank=True, max_length=127, null=True)),
                ('party', models.CharField(blank=True, max_length=127, null=True)),
                ('bill_number', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='PressStatementTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congress', models.CharField(max_length=127)),
                ('bill_number', models.CharField(max_length=127)),
                ('status', models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], db_index=True, default='PENDING', help_text='Current state of the press statement task.', max_length=50, verbose_name='Task State')),
                ('task_id', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=127)),
                ('bill_id', models.CharField(blank=True, max_length=127, null=True)),
                ('bill_title', models.TextField(blank=True, null=True)),
                ('congress', models.CharField(max_length=10)),
                ('date_issued', models.CharField(max_length=35)),
                ('permanent_pdf_link', models.FileField(blank=True, null=True, upload_to='statements/')),
                ('original_pdf_link', models.CharField(blank=True, max_length=255, null=True)),
                ('administration', models.CharField(default='common', max_length=100)),
                ('date_fetched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cosponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name_first', models.CharField(blank=True, max_length=250, null=True)),
                ('name_last', models.CharField(blank=True, max_length=250, null=True)),
                ('name_full_official', models.CharField(blank=True, max_length=250, null=True)),
                ('bioguide_id', models.CharField(blank=True, max_length=100, null=True)),
                ('thomas', models.CharField(blank=True, max_length=100, null=True)),
                ('party', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('type', models.CharField(blank=True, max_length=3, null=True)),
                ('terms', models.JSONField(default=list)),
                ('committees', models.JSONField(blank=True, default=list, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('name', 'bioguide_id')},
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thomas_id', models.CharField(db_index=True, max_length=10, unique=True)),
                ('type', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True, null=True)),
                ('minority_url', models.URLField(blank=True, null=True)),
                ('house_committee_id', models.CharField(blank=True, max_length=10, null=True)),
                ('jurisdiction', models.CharField(blank=True, max_length=250, null=True)),
                ('cosponsors', models.ManyToManyField(blank=True, to='bills.Cosponsor')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_congress_type_number', models.CharField(db_index=True, max_length=100, unique=True)),
                ('type', models.CharField(blank=True, max_length=40, null=True)),
                ('congress', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=5, null=True)),
                ('titles', models.JSONField(default=list)),
                ('summary', models.TextField(blank=True, null=True)),
                ('titles_whole_bill', models.JSONField(default=list)),
                ('short_title', models.TextField(blank=True, null=True)),
                ('sponsor', models.JSONField(default=dict)),
                ('related_bills', models.JSONField(default=list)),
                ('related_dict', models.JSONField(default=dict)),
                ('cosponsors_dict', models.JSONField(default=list)),
                ('committees_dict', models.JSONField(default=list)),
                ('es_similarity', models.JSONField(default=list)),
                ('es_similar_bills_dict', models.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cosponsors', models.ManyToManyField(blank=True, to='bills.Cosponsor')),
            ],
        ),
    ]
