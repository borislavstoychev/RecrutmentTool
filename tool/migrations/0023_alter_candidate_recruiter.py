# Generated by Django 3.2.6 on 2021-10-29 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0022_auto_20211029_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tool.recruiter'),
        ),
    ]
