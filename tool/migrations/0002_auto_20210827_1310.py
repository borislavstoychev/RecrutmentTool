# Generated by Django 3.2.6 on 2021-08-27 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='recruiter',
            name='name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.skills'),
        ),
        migrations.AlterField(
            model_name='job',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.skills'),
        ),
    ]
