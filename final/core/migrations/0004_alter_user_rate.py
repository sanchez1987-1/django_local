# Generated by Django 4.0.4 on 2022-06-01 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_rate_linked_by_user_rate_delete_rateuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rate',
            field=models.ForeignKey(db_column='rate_id', default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.rate', verbose_name='Rate'),
        ),
    ]
