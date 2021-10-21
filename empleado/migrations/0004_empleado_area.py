# Generated by Django 3.2.8 on 2021-10-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_delete_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='area',
            field=models.IntegerField(choices=[(1, 'Administracion'), (2, 'Ventas'), (3, 'Desarrollo'), (4, 'Medicina')], default=1),
        ),
    ]
