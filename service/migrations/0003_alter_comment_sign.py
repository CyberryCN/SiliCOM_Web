# Generated by Django 5.1.6 on 2025-03-05 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_sign_nick_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="sign",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="service.sign",
                verbose_name="关联报名",
            ),
        ),
    ]
