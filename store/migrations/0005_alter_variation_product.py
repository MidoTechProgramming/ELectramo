# Generated by Django 5.0.6 on 2024-07-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_variation_product_variation_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ManyToManyField(blank=True, to='store.product'),
        ),
    ]
