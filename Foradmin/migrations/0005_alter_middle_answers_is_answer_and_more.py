# Generated by Django 5.0.2 on 2024-02-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foradmin', '0004_alter_users_entry_count_alter_users_high_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='middle_answers',
            name='is_answer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='middle_answers',
            name='is_true',
            field=models.BooleanField(default=False),
        ),
    ]
