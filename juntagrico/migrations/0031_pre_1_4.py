# Generated by Django 3.1.5 on 2021-01-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico', '0030_auto_20201112_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cancellation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Kündigungsdatum'),
        ),
    ]
