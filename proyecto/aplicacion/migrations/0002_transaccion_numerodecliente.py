# Generated by Django 4.2.10 on 2024-03-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='numeroDeCliente',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]