# Generated by Django 4.2.3 on 2023-08-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_alter_segment_first_match_alter_segment_last_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
