# Generated by Django 3.0.3 on 2022-11-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carComm_app', '0002_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='registration',
            field=models.CharField(default='XXXXX', max_length=10),
            preserve_default=False,
        ),
    ]
