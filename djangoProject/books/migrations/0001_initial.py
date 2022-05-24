# Generated by Django 4.0.4 on 2022-05-24 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('num_pages', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('type', models.CharField(blank=True, choices=[('BULLET', 'BULLET'), ('FOOD', 'FOOD'), ('TRAVEL', 'TRAVEL'), ('SPORT', 'SPORT')], default='BULLET', max_length=50)),
                ('publisher', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
