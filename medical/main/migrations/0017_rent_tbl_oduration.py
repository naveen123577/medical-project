# Generated by Django 5.0.2 on 2024-03-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rent_tbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent_tbl',
            name='oduration',
            field=models.IntegerField(default=2),
        ),
    ]
