# Generated by Django 5.1.4 on 2024-12-14 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demons", "0006_qrcode_is_registered_tempvisitor_registered_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visitor",
            name="qr_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="demons.qrcode",
            ),
        ),
    ]
