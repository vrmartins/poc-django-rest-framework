# Generated by Django 3.0.3 on 2020-04-11 14:53

import core.utils.cnpj_is_valid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=14, unique=True, validators=[core.utils.cnpj_is_valid.cnpj_is_valid])),
            ],
        ),
    ]
