# Generated by Django 4.0.2 on 2022-05-12 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flats', '0008_user_remove_house_date_remove_house_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='condition',
            field=models.TextField(default='The condition is  '),
        ),
        migrations.AlterField(
            model_name='house',
            name='view',
            field=models.TextField(default='The view is '),
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Roles',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.roles')),
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
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.roles')),
            ],
        ),
    ]
