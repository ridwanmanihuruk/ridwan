# Generated by Django 3.2.6 on 2021-08-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_category_champaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='headerimg',
            field=models.ImageField(default=None, upload_to='static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='motto',
            field=models.TextField(default='Input Motto'),
        ),
    ]
