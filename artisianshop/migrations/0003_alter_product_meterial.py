# Generated by Django 5.0 on 2023-12-31 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisianshop', '0002_remove_product_type_product_meterial_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Meterial',
            field=models.CharField(choices=[('Wood', 'Wood'), ('Metal', 'Metal'), ('Fabric', 'Fabric'), ('Paper', 'Paper'), ('Leather', 'Leather'), ('Cloth', 'Cloth'), ('Recycled Meterials', 'Recycled Meterials'), ('Kitchen', 'Kitchen'), ('Other', 'Other')], default='Wood', max_length=100),
        ),
    ]
