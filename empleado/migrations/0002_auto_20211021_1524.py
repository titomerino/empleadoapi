# Generated by Django 3.2.8 on 2021-10-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='titulo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='documento',
            field=models.CharField(max_length=50, verbose_name='Nº de documento'),
        ),
    ]
