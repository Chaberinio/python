# Generated by Django 4.1.1 on 2022-10-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_music_app', '0003_alter_artist_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='surname',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
    ]
