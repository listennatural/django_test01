# Generated by Django 2.1.2 on 2018-11-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.IntegerField(help_text='所属批次'),
        ),
    ]
