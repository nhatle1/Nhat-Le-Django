# Generated by Django 3.2 on 2021-04-19 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order_orderitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='static/images')),
                ('productType', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='BangTuongTacProduct',
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product'),
        ),
    ]
