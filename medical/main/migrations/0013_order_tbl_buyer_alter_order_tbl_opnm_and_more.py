# Generated by Django 5.0.2 on 2024-02-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_des_order_tbl_odes_rename_pnm_order_tbl_opnm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_tbl',
            name='Buyer',
            field=models.CharField(default='user', max_length=25),
        ),
        migrations.AlterField(
            model_name='order_tbl',
            name='opnm',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='order_tbl',
            name='oseller',
            field=models.CharField(max_length=225),
        ),
    ]
