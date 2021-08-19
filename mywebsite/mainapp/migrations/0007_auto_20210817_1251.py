# Generated by Django 3.2.6 on 2021-08-17 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210816_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_pict', models.ImageField(upload_to='static/images/header')),
            ],
        ),
        migrations.CreateModel(
            name='Pict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_pict', models.ImageField(upload_to='static/images/products')),
                ('pict_1', models.ImageField(upload_to='static/images/products')),
                ('pict_2', models.ImageField(upload_to='static/images/products')),
                ('pict_3', models.ImageField(upload_to='static/images/products')),
                ('pict_4', models.ImageField(upload_to='static/images/products')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='headerimg',
        ),
        migrations.AddField(
            model_name='category',
            name='Header_pict',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.header'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Pict',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.pict'),
            preserve_default=False,
        ),
    ]
