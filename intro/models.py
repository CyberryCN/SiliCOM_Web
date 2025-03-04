# introduction/models.py
from django.db import models
import os

class Operator(models.Model):
    management_name = models.CharField(
        max_length=100, 
        verbose_name="社长姓名",
        default="佚名"
    )
    management_campus = models.CharField(
        max_length=120, 
        verbose_name="所属学院",
        default="未知"
    )
    management_time = models.CharField(
        max_length=100, 
        verbose_name="任期时间",
        default="未知"
    )
    photo = models.ImageField(
        upload_to='operators/',  # 文件将保存到 introduction/media/operators/
        verbose_name="社长照片",
        blank=True
    )
    introduction = models.TextField(
        verbose_name="人物简介",
        default="无"
    )
    op_id = models.IntegerField(
        unique=True,
        verbose_name="社长编号",
        help_text="唯一标识符"
    )

    @property
    def photo_path(self):
        """动态生成图片路径"""
        if self.photo:  # 优先使用上传的图片
            return self.photo.url
        # 回退到静态目录的默认图片
        return f'/static/introduction/images/{self.op_id}.png'

    def save(self, *args, **kwargs):
        """自动重命名上传的图片"""
        if self.photo and not self.photo.name.startswith(f'operator_{self.op_id}'):
            # 获取文件扩展名
            ext = os.path.splitext(self.photo.name)[1]
            # 生成新文件名
            self.photo.verbose_name = f'operator_{self.op_id}{ext}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.op_id} - {self.management_name}"
