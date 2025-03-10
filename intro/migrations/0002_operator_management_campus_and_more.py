# Generated by Django 5.1.6 on 2025-03-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("introduction", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="operator",
            name="management_campus",
            field=models.CharField(
                default="未知", help_text="社长所在学院", max_length=120
            ),
        ),
        migrations.AlterField(
            model_name="operator",
            name="introduction",
            field=models.TextField(default="无", help_text="介绍文本"),
        ),
        migrations.AlterField(
            model_name="operator",
            name="management_name",
            field=models.CharField(
                default="佚名", help_text="历代社长名字", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="operator",
            name="management_time",
            field=models.CharField(
                default="未知", help_text="“在位”时间", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="operator",
            name="op_id",
            field=models.IntegerField(
                default=0, help_text="唯一性检索标定", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="operator",
            name="photo_path",
            field=models.CharField(
                default="./", help_text="存放对应介绍图片的地址", max_length=255
            ),
        ),
    ]
