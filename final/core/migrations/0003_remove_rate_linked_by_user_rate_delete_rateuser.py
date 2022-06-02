# Generated by Django 4.0.4 on 2022-06-01 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_devices_device_rename_rateusers_rateuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='linked_by',
        ),
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.ForeignKey(db_column='rate_id', default='', on_delete=django.db.models.deletion.CASCADE, to='core.rate', verbose_name='Rate'),
        ),
        migrations.DeleteModel(
            name='RateUser',
        ),
    ]
