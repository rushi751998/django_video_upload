# Generated by Django 3.2.7 on 2023-02-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='person_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_id', models.IntegerField(default=0)),
                ('gender', models.CharField(default='', max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('emotion', models.CharField(default='', max_length=20)),
                ('race', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
