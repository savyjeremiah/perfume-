# Generated by Django 5.1.4 on 2025-04-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_perfume_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfume',
            options={'verbose_name_plural': 'Perfumes'},
        ),
        migrations.AlterField(
            model_name='perfume',
            name='category',
            field=models.CharField(choices=[('Designers Perfume Oil', 'Designers Perfume Oil'), ('Suratti Perfume Oils', 'Suratti Perfume Oils'), ('Naseem Oils', 'Naseem Oils')], max_length=150),
        ),
    ]
