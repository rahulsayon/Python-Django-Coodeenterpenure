# Generated by Django 3.0.3 on 2020-04-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200405_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
