# Generated by Django 3.2 on 2021-05-05 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210502_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order'),
        ),
    ]
