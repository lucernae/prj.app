# Generated by Django 2.2 on 2019-12-04 03:13

import changes.models.sponsor
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this category.', max_length=255)),
                ('sort_number', models.SmallIntegerField(default=0, help_text='The order in which this category is listed within a project')),
                ('slug', models.SlugField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'project'), ('project', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of sponsor.', max_length=255)),
                ('contact_title', models.CharField(blank=True, help_text='Title of the sponsorship representative i.e Treasurer.', max_length=255, null=True, verbose_name='Sponsorship Representative Title')),
                ('sponsor_url', models.CharField(blank=True, help_text='Input the sponsor URL.', max_length=255, null=True)),
                ('contact_person', models.CharField(blank=True, help_text='Input the contact person of sponsor.', max_length=255, null=True)),
                ('address', models.TextField(blank=True, help_text='Enter the complete street address for this sponsor. Use line breaks to separate address elements and use the country field to specify the country.', null=True)),
                ('country', django_countries.fields.CountryField(blank=True, help_text='Select the country for this sponsor', max_length=2, null=True)),
                ('sponsor_email', models.CharField(blank=True, help_text='Input an email of sponsor.', max_length=255, null=True, validators=[changes.models.sponsor.validate_email_address])),
                ('agreement', models.FileField(blank=True, help_text='Attach sponsor agreement', upload_to='docs')),
                ('logo', models.ImageField(help_text='An image of sponsor logo e.g. a splashscreen. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to='images/projects')),
                ('approved', models.BooleanField(default=False, help_text='Whether this sponsor has been approved for use by the project owner.')),
                ('invoice_number', models.CharField(blank=True, help_text='Invoice number for the sponsor.', max_length=255, null=True, verbose_name='Sponsorship invoice number')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project')),
            ],
            options={
                'ordering': ['project', 'name'],
                'unique_together': {('name', 'project'), ('project', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='SponsorshipLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of sponsorship level. e.g. Gold, Bronze, etc', max_length=255)),
                ('value', models.IntegerField(help_text='Amount of money associated with this sponsorship level.')),
                ('currency', models.CharField(help_text='The currency which associated with this sponsorship level.', max_length=255)),
                ('logo', models.ImageField(help_text='An image of sponsorship level logo e.g. a bronze medal.Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to='images/projects')),
                ('logo_width', models.IntegerField(default=100, help_text='Enter the width of the icon that should be used on the changelog')),
                ('logo_height', models.IntegerField(default=100, help_text='Enter the height of the icon that should be used on the changelog')),
                ('approved', models.BooleanField(default=False, help_text='Whether this sponsorship level has been approved for use by the project owner.')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project')),
            ],
            options={
                'ordering': ['project', '-value'],
                'unique_together': {('name', 'project'), ('project', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this release e.g. 1.0.1.', max_length=255)),
                ('padded_version', models.CharField(blank=True, help_text='Numeric version for this release e.g. 001000001 for 1.0.1 calculated by zero padding each component of maj/minor/bugfix elements from name.', max_length=9)),
                ('image_file', models.ImageField(blank=True, help_text='An optional image for this version e.g. a splashscreen. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to='images/projects')),
                ('description', models.TextField(blank=True, help_text='Describe the new version. Markdown is supported.', null=True)),
                ('release_date', models.DateField(blank=True, help_text='Date of official release', null=True, verbose_name='Release date (yyyy-mm-dd)')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project')),
            ],
            options={
                'unique_together': {('name', 'project'), ('slug', 'project')},
            },
        ),
        migrations.CreateModel(
            name='SponsorshipPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now, help_text='Start date of sponsorship period', verbose_name='Start date')),
                ('end_date', models.DateField(default=django.utils.timezone.now, help_text='End date of sponsorship period', verbose_name='End date')),
                ('amount_sponsored', models.DecimalField(blank=True, decimal_places=2, help_text='The actual amount sponsored for this period.', max_digits=30, null=True, verbose_name='Amount Sponsored')),
                ('currency', models.CharField(blank=True, default='EUR', help_text='The currency that is used for sponsorship payment.', max_length=50, null=True)),
                ('approved', models.BooleanField(default=False, help_text='Whether this sponsorship period has been approved for use by the project owner.')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project')),
                ('sponsor', models.ForeignKey(help_text='Input the sponsor name', on_delete=django.db.models.deletion.CASCADE, to='changes.Sponsor')),
                ('sponsorship_level', models.ForeignKey(help_text='This level take from Sponsorship Level, you can add it by using Sponsorship Level menu', on_delete=django.db.models.deletion.CASCADE, to='changes.SponsorshipLevel')),
            ],
            options={
                'ordering': ['project', '-end_date'],
                'unique_together': {('project', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField(default=0, help_text='The order in which this entry is listed within the category.', verbose_name='Entry number')),
                ('title', models.CharField(help_text='Feature title for this changelog entry.', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Describe the new feature. Markdown is supported.', null=True)),
                ('image_file', models.ImageField(blank=True, help_text='A image that is related to this visual changelog entry. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to='images/entries')),
                ('image_credits', models.CharField(blank=True, help_text='Who should be credited for this image?', max_length=255, null=True)),
                ('video', embed_video.fields.EmbedVideoField(blank=True, help_text='Paste your youtube video link', null=True, verbose_name='Youtube video')),
                ('funded_by', models.CharField(blank=True, help_text='Input the funder name.', max_length=255, null=True)),
                ('funder_url', models.CharField(blank=True, help_text='Input the funder URL.', max_length=255, null=True)),
                ('developed_by', models.CharField(blank=True, help_text='Input the developer name.', max_length=255, null=True)),
                ('developer_url', models.CharField(blank=True, help_text='Input the developer URL.', max_length=255, null=True)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changes.Category')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changes.Version')),
            ],
            options={
                'ordering': ['version', 'category', 'sequence_number'],
                'unique_together': {('version', 'slug'), ('title', 'version', 'category')},
            },
        ),
    ]
