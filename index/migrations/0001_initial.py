# Generated by Django 2.1.2 on 2018-11-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(help_text='项目名称', max_length=255)),
                ('project_img', models.CharField(help_text='项目图片', max_length=255)),
                ('project_link', models.CharField(help_text='项目链接', max_length=255)),
            ],
        ),
    ]
