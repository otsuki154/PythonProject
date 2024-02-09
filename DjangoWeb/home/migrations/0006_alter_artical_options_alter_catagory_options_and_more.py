# Generated by Django 5.0.1 on 2024-02-09 07:38

import home.custom_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_feed_alter_artical_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artical',
            options={'verbose_name_plural': 'Articals'},
        ),
        migrations.AlterModelOptions(
            name='catagory',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='feed',
            options={'verbose_name_plural': 'Feeds'},
        ),
        migrations.AlterField(
            model_name='artical',
            name='special',
            field=home.custom_field.CustomBooleanField(),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='is_homepage',
            field=home.custom_field.CustomBooleanField(),
        ),
    ]
