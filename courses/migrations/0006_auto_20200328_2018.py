# Generated by Django 3.0.4 on 2020-03-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cover_img',
            field=models.ImageField(upload_to='coverImage'),
        ),
    ]
