# Generated by Django 3.2.6 on 2021-08-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210814_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='champaign',
            field=models.TextField(default='Input Champaign'),
        ),
    ]
