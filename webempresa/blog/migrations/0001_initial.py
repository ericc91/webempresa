# Generated by Django 4.2.8 on 2023-12-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
        ),
    ]
