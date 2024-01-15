# Generated by Django 5.0.1 on 2024-01-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
