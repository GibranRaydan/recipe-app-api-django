# Generated by Django 3.2.23 on 2023-11-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=255)),
            ],
        ),
    ]
