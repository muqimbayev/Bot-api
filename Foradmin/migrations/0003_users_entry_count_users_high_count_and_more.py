# Generated by Django 5.0.2 on 2024-02-26 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foradmin', '0002_alter_entry_answers_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='entry_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='high_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='middle_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='puzzle_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='high_answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Foradmin.users'),
        ),
        migrations.AlterField(
            model_name='middle_answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Foradmin.users'),
        ),
        migrations.AlterField(
            model_name='puzzle_answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Foradmin.users'),
        ),
    ]
