# Generated by Django 4.0.2 on 2022-05-31 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property_type',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]