# Generated by Django 4.2.5 on 2023-09-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MyPerson',
            fields=[
            ],
            options={
                'ordering': ['first_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('MyApp.person',),
        ),
    ]
