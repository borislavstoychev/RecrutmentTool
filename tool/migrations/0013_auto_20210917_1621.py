# Generated by Django 3.2.6 on 2021-09-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0012_remove_candidate_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(to='tool.Skills'),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='tool.Skills'),
        ),
    ]
