# Generated by Django 4.1 on 2022-08-04 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_cart_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Total_price',
            new_name='total_price',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='basket.cart')),
            ],
        ),
    ]