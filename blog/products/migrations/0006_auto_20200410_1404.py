# Generated by Django 3.0.3 on 2020-04-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200405_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=False),
        ),
    ]
