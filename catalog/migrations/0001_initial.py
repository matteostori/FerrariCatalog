# Generated by Django 3.2.3 on 2021-09-04 15:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this car', primary_key=True, serialize=False)),
                ('order', models.IntegerField()),
                ('name', models.CharField(help_text='Enter the name of the car', max_length=50)),
                ('caryear', models.DateField(help_text='Enter the car date')),
                ('color', models.CharField(blank=True, choices=[('yl', 'Yellow'), ('bk', 'Black'), ('bl', 'Blue'), ('rd', 'Red')], default='rd', help_text='Car color', max_length=2)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the pilot', max_length=50)),
                ('firstrace', models.DateField(help_text='Enter the date of the first race')),
                ('description', models.TextField(help_text='Enter a description')),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(help_text='Enter image path', max_length=50)),
                ('description', models.TextField(help_text='Enter a description')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='pilot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.pilot'),
        ),
    ]
