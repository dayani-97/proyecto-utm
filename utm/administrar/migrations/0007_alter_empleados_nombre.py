# Generated by Django 3.2.4 on 2021-08-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrar', '0006_alter_empleados_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
    ]
