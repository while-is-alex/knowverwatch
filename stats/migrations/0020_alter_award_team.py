# Generated by Django 4.2.3 on 2023-09-16 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0019_alter_award_player_alter_award_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='awards', to='stats.team'),
        ),
    ]
