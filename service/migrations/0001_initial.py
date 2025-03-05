# Generated by Django 5.1.6 on 2025-03-05 04:11

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "activity_id",
                    models.AutoField(
                        help_text="活动唯一标识符",
                        primary_key=True,
                        serialize=False,
                        verbose_name="活动编号",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="活动名称")),
                ("activity_time", models.DateTimeField(verbose_name="活动时间")),
                ("limit_time", models.DateTimeField(verbose_name="报名截止时间")),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="报名开放状态"),
                ),
            ],
            options={
                "verbose_name_plural": "活动列表",
                "ordering": ["-activity_time"],
            },
        ),
        migrations.CreateModel(
            name="Sign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unique_code",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "machine",
                    models.CharField(
                        help_text="例如：联想拯救者Y7000 2023款",
                        max_length=100,
                        verbose_name="电脑型号",
                    ),
                ),
                ("requirement", models.TextField(verbose_name="具体需求")),
                (
                    "phone_number",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator("^\\+?1?\\d{9,15}$")
                        ],
                        verbose_name="联系电话",
                    ),
                ),
                (
                    "sign_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="报名时间"),
                ),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="signups",
                        to="service.activity",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "报名记录",
                "ordering": ["-sign_time"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="服务评分",
                    ),
                ),
                ("content", models.TextField(verbose_name="评价内容")),
                (
                    "comment_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="评价时间"),
                ),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="service.activity",
                    ),
                ),
                (
                    "sign",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback",
                        to="service.sign",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "用户评价",
                "ordering": ["-comment_time"],
            },
        ),
    ]
