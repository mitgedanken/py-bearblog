# Generated by Django 3.2.23 on 2024-10-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0033_auto_20241022_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alias',
            field=models.CharField(blank=True, db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='hidden',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_page',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='make_discoverable',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
