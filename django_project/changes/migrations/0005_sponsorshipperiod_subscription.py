# Generated by Django 2.2 on 2019-12-18 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0004_2_1'),
        ('changes', '0004_auto_20191217_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorshipperiod',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Subscription'),
        ),
    ]
