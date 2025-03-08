# Generated by Django 5.1.6 on 2025-03-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RecruitmentDoc",
            fields=[
                (
                    "document",
                    models.FileField(
                        blank=True,
                        upload_to="recruitment_docs",
                        verbose_name="招新报表",
                    ),
                ),
                ("doc_label", models.CharField(max_length=100, verbose_name="文件名")),
                (
                    "doc_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="文件编号"
                    ),
                ),
            ],
        ),
    ]
