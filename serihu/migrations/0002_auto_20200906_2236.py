# Generated by Django 3.1 on 2020-09-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serihu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serihu',
            name='serihu',
            field=models.CharField(max_length=500),
        ),
    ]
