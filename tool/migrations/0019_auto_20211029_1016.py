# Generated by Django 3.2.6 on 2021-10-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0018_alter_interview_candidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='username',
        ),
        migrations.AddField(
            model_name='recruiter',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recruiter',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recruiter',
            name='last_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
