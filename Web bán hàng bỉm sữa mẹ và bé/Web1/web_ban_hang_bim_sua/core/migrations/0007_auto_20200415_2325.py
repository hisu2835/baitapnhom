# Generated by Django 2.2.4 on 2020-04-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(help_text='Size: 1920x570', upload_to=''),
        ),
    ]
