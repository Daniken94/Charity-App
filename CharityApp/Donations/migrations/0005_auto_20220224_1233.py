# Generated by Django 3.2.10 on 2022-02-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donations', '0004_donations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donations',
            options={'verbose_name_plural': 'Donations'},
        ),
        migrations.AlterField(
            model_name='donations',
            name='quantity',
            field=models.IntegerField(verbose_name='Podal liczbe worków 60l z podarunkami.'),
        ),
    ]