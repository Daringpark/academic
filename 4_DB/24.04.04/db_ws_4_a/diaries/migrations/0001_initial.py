# Generated by Django 4.2.9 on 2024-04-04 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=125)),
                ('picture', models.ImageField(blank=True, upload_to='diary/%y/%b/%a')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=125)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaries.diary')),
            ],
        ),
    ]
