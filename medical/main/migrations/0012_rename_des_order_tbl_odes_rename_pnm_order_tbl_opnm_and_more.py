# Generated by Django 5.0.2 on 2024-02-23 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_order_tbl_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_tbl',
            old_name='des',
            new_name='odes',
        ),
        migrations.RenameField(
            model_name='order_tbl',
            old_name='pnm',
            new_name='opnm',
        ),
        migrations.RenameField(
            model_name='order_tbl',
            old_name='prc',
            new_name='oprc',
        ),
        migrations.RenameField(
            model_name='order_tbl',
            old_name='seller',
            new_name='oseller',
        ),
    ]
