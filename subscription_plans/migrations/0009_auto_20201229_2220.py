# Generated by Django 3.1.4 on 2020-12-29 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0008_exercisesplan_how_it_works'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisesplan',
            name='description_3',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_1',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_2',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_3',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_4',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_5',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_6',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
        migrations.AlterField(
            model_name='exercisesplan',
            name='source_7',
            field=models.TextField(blank=True, max_length=1400, null=True),
        ),
    ]
