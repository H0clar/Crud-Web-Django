# Generated by Django 3.2.8 on 2023-09-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='Img/', verbose_name='Imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
