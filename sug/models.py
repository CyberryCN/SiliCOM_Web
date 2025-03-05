from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Level(models.Model):
    level_id = models.PositiveIntegerField(
        primary_key=True,
        verbose_name='价位编号',
        help_text='用于URL的价位段标识（示例：1代表3000元以下）'
    )
    level_range = models.CharField(
        max_length=50,
        verbose_name='价格区间',
        help_text='示例：3000-5000元'
    )

    class Meta:
        verbose_name = '价格等级'
        verbose_name_plural = verbose_name
        ordering = ['level_id']

    def __str__(self):
        return f"{self.level_range}（ID：{self.level_id}）"

class Book(models.Model):
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='所属价位'
    )
    book_label = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='产品标签',
        help_text='仅包含英文数字的URL友好标识（示例：lenovo-yoga）'
    )
    book_name = models.CharField(
        max_length=100,
        verbose_name='产品名称'
    )
    book_preview = models.ImageField(
        upload_to='previews/',  # 相对路径
        verbose_name='产品预览图',
        blank=True,
        null=True,
        help_text='图片将存储在 static/suggestion/images/previews/',
    )
    book_cpu = models.CharField(
        max_length=100,
        verbose_name="处理器"
    )
    book_gpu = models.CharField(
        max_length=100,
        verbose_name='显卡'
    )
    book_detail = models.TextField(
        verbose_name="详细配置"
    )
    book_crowd = models.TextField(
        verbose_name='适用人群'
    )

    class Meta:
        verbose_name = '笔记本推荐'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['book_label'], name='book_label_idx')
        ]

    def __str__(self):
        return f"{self.book_name} - {self.level.level_range}"

    def save(self, *args, **kwargs):
        if not self.book_label:
            self.book_label = slugify(self.book_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('sug:book-detail', kwargs={
            'level_id': self.level.level_id,
            'book_label': self.book_label
        })