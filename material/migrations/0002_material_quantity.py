# Generated by Django 3.0.7 on 2020-11-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
            preserve_default=False,
        ),
    ]
