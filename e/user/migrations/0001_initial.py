# Generated by Django 5.0.3 on 2024-04-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ph', models.CharField(blank=True, max_length=10, null=True)),
                ('add', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
