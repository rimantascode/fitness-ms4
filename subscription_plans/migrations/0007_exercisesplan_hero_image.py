# Generated by Django 3.1.4 on 2020-12-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0006_exercisesplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisesplan',
            name='hero_image',
            field=models.URLField(blank=True, max_length=1400, null=True),
        ),
    ]