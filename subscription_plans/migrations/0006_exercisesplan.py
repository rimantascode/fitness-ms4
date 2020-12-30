# Generated by Django 3.1.4 on 2020-12-29 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0005_auto_20201229_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='exercisesPlan',
            fields=[
                ('has_access', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='subscription_plans.subscriptions')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('directions', models.TextField(max_length=2000)),
                ('day_1', models.CharField(blank=True, max_length=200, null=True)),
                ('source_1', models.URLField(blank=True, max_length=1400, null=True)),
                ('description_1', models.TextField(max_length=2000)),
                ('day_2', models.CharField(blank=True, max_length=200, null=True)),
                ('source_2', models.URLField(blank=True, max_length=1400, null=True)),
                ('description_2', models.TextField(max_length=2000)),
                ('day_3', models.CharField(blank=True, max_length=200, null=True)),
                ('source_3', models.URLField(blank=True, max_length=1400, null=True)),
                ('day_4', models.CharField(blank=True, max_length=200, null=True)),
                ('source_4', models.URLField(blank=True, max_length=1400, null=True)),
                ('description_4', models.TextField(max_length=2000)),
                ('day_5', models.CharField(blank=True, max_length=200, null=True)),
                ('source_5', models.URLField(blank=True, max_length=1400, null=True)),
                ('description_5', models.TextField(max_length=2000)),
                ('day_6', models.CharField(blank=True, max_length=200, null=True)),
                ('source_6', models.URLField(blank=True, max_length=1400, null=True)),
                ('description_6', models.TextField(max_length=2000)),
                ('day_7', models.CharField(blank=True, max_length=200, null=True)),
                ('source_7', models.URLField(blank=True, max_length=1400, null=True)),
                ('description_7', models.TextField(max_length=2000)),
            ],
        ),
    ]