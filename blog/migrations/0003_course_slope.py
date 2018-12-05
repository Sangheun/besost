# Generated by Django 2.1.4 on 2018-12-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_description', models.TextField()),
                ('course_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Slope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slope_name', models.CharField(max_length=200)),
                ('slope_description', models.TextField()),
                ('slope_image', models.ImageField(upload_to='')),
            ],
        ),
    ]