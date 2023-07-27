# Generated by Django 4.1.4 on 2023-07-27 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.CharField(default='S', max_length=10)),
                ('userName', models.EmailField(max_length=254)),
                ('userPassword', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImg', models.ImageField(upload_to='')),
                ('specilization', models.CharField(max_length=200)),
                ('course', models.CharField(default='IELTS', max_length=200)),
                ('qulification', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to='home.login')),
            ],
        ),
    ]