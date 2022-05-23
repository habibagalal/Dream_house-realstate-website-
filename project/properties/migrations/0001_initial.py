# Generated by Django 4.0.2 on 2022-05-18 23:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('h', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(null=True, upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('condition', models.TextField(default='The condition is  ')),
                ('floors', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('view', models.TextField(default='The view is ')),
                ('lat', models.IntegerField()),
                ('SQFT_Living', models.IntegerField()),
                ('SQFT_above', models.IntegerField()),
                ('SQFT_basement', models.IntegerField()),
                ('SQFT_lot15', models.IntegerField()),
                ('SQFT_living15', models.IntegerField()),
                ('yr_renovated', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Property',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='property_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.roles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('postalcode', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField(null=True)),
                ('phone', models.IntegerField()),
                ('age', models.PositiveIntegerField(null=True)),
                ('gender', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
