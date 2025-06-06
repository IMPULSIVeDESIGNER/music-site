# Generated by Django 5.1.3 on 2025-05-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='songs/')),
                ('size', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('download_count', models.IntegerField(default=0)),
            ],
        ),
    ]
