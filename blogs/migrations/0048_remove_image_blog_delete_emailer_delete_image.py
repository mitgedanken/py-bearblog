# Generated by Django 4.0.4 on 2022-05-27 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0047_auto_20220526_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Emailer',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
