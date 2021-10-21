# Generated by Django 3.2.7 on 2021-10-20 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('description', models.TextField(verbose_name='description')),
                ('category', models.CharField(max_length=50, verbose_name='category')),
                ('tags', models.CharField(default='', max_length=130)),
                ('price', models.FloatField(default=0.0)),
                ('public_id', models.CharField(default='1c9c0c82-df13-4d69-9452-f734dda6c39a', max_length=300)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('discount', models.BooleanField(default=False)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('rating', models.CharField(default='[1]', max_length=1300)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('verified', models.BooleanField(default=False)),
                ('public_id', models.CharField(default='5eb5dce8-c9a2-4737-835d-8bd708aad7d8', max_length=300)),
                ('rating', models.CharField(default='[1]', max_length=1300)),
                ('user_id', models.IntegerField(default=1000000)),
                ('enrolled_courses', models.TextField(default='{}')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.IntegerField(default=0)),
                ('links', models.CharField(default='[]', max_length=33)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tutor.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tutor.tutor'),
        ),
    ]