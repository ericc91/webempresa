# Generated by Django 4.2.8 on 2023-12-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_link_options_link_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='key',
            field=models.SlugField(default=True, max_length=100, unique=True, verbose_name='Nombre clave'),
        ),
    ]
