# Generated by Django 4.1.1 on 2022-10-06 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=512)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆☆☆☆☆☆'), (2, '★★☆☆☆☆☆☆☆☆'), (3, '★★★☆☆☆☆☆☆☆'), (4, '★★★★☆☆☆☆☆☆'), (5, '★★★★★☆☆☆☆☆'), (6, '★★★★★★☆☆☆☆'), (7, '★★★★★★★☆☆☆'), (8, '★★★★★★★★☆☆'), (9, '★★★★★★★★★☆'), (10, '★★★★★★★★★★')]),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games_app.platform'),
        ),
    ]
