# Generated by Django 4.1.7 on 2023-05-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_price_product_selling_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_rate',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
