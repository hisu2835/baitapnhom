# Generated by Django 5.1.4 on 2025-02-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_billingaddress_id_alter_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock_no',
            field=models.IntegerField(default=0),
        ),
    ]
