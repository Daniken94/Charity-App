# Generated by Django 3.2.10 on 2022-02-24 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donations', '0003_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('city', models.CharField(max_length=120, verbose_name='Podaj miasto.')),
                ('street', models.CharField(max_length=120, verbose_name='Podaj nazwę ulicy.')),
                ('home_number', models.IntegerField(verbose_name='Podaj numer domu/mieszkania.')),
                ('phone_number', models.IntegerField()),
                ('zip_code', models.CharField(default='42680', max_length=5, verbose_name='Podaj kod pocztowy.')),
                ('pick_up_date', models.DateField(verbose_name='Paczka będzie gotowa do odbioru dnia: ')),
                ('pick_up_time', models.TimeField(verbose_name='Paczka będzie gotowa do odbioru o godzinie: ')),
                ('pick_up_comment', models.TextField(max_length=240, verbose_name='Komentarz dla kuriera')),
                ('categories', models.ManyToManyField(to='Donations.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Donations.institution')),
                ('user', models.ForeignKey(default=django.forms.fields.NullBooleanField, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
