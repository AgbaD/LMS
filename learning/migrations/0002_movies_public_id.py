# Generated by Django 3.2.7 on 2021-10-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='public_id',
            field=models.CharField(default=-1, max_length=300),
            preserve_default=False,
        ),
    ]
