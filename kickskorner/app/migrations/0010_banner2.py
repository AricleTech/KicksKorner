# Generated by Django 4.1.7 on 2023-05-02 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_product2_delete_product3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50)),
                ('title2', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=50)),
                ('price2', models.CharField(max_length=50)),
            ],
        ),
    ]