# Generated by Django 3.1.4 on 2021-01-06 20:54

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
            name='exercisesPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_it_works', models.TextField(blank=True, max_length=2000)),
                ('hero_image', models.URLField(blank=True, max_length=1400, null=True)),
                ('name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
                ('directions', models.TextField(max_length=2000)),
                ('day_1', models.CharField(blank=True, max_length=200, null=True)),
                ('source_1', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_1', models.TextField(blank=True, max_length=2000)),
                ('day_2', models.CharField(blank=True, max_length=200, null=True)),
                ('source_2', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_2', models.TextField(blank=True, max_length=2000)),
                ('day_3', models.CharField(blank=True, max_length=200, null=True)),
                ('source_3', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_3', models.TextField(blank=True, max_length=2000)),
                ('day_4', models.CharField(blank=True, max_length=200, null=True)),
                ('source_4', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_4', models.TextField(blank=True, max_length=2000)),
                ('day_5', models.CharField(blank=True, max_length=200, null=True)),
                ('source_5', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_5', models.TextField(blank=True, max_length=2000)),
                ('day_6', models.CharField(blank=True, max_length=200, null=True)),
                ('source_6', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_6', models.TextField(blank=True, max_length=2000)),
                ('day_7', models.CharField(blank=True, max_length=200, null=True)),
                ('source_7', models.TextField(blank=True, max_length=1400, null=True)),
                ('description_7', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerIdstripe', models.CharField(max_length=255)),
                ('SubscriptionIdstripe', models.CharField(max_length=255)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('subscription_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
