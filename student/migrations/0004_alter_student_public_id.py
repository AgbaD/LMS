# Generated by Django 3.2.7 on 2021-10-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='public_id',
            field=models.CharField(default='eaa4f063-6317-4e1a-b5f0-60696a550b78', max_length=300),
        ),
    ]