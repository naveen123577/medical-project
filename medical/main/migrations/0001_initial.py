# Generated by Django 5.0.2 on 2024-02-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnm', models.CharField(max_length=25)),
                ('pim', models.FileField(upload_to='pic')),
                ('prc', models.IntegerField()),
                ('des', models.TextField()),
            ],
        ),
    ]
