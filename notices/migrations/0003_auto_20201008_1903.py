# Generated by Django 3.1.2 on 2020-10-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]