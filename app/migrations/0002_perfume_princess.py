# Generated by Django 5.1.4 on 2025-04-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='princess',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
