# Generated by Django 3.2.6 on 2021-09-17 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0011_candidate_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='skills',
        ),
    ]