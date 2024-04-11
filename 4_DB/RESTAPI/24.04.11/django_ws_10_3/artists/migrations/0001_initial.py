# Generated by Django 4.2.8 on 2024-04-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('agency', models.TextField()),
                ('debut_date', models.DateField()),
                ('is_group', models.BooleanField()),
            ],
        ),
    ]