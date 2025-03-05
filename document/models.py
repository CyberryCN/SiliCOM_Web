from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Board(models.Model):
    board_id = models.IntegerField(
        primary_key=True,
        verbose_name="板块编号",
        help_text="板块唯一标识符，自动递增"
    )
    board_title = models.CharField(
        max_length=100,
        verbose_name="板块文字",
        default="新板块",
    )

    class Meta:
        verbose_name = "文章板块"
        verbose_name_plural = verbose_name
        ordering = ['board_id']  # 按编号排序

    def __str__(self):
        return f"{self.board_id} - {self.board_title}"

    def get_absolute_url(self):
        return reverse('board-detail', kwargs={'board_id': self.board_id})

class Entry(models.Model):
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        verbose_name="所属板块",
        related_name="entries",  # 重要！方便反向查询
        help_text="选择文章归属的板块"
    )
    entry_title = models.CharField(
        max_length=100,
        verbose_name="文章名字",
        default="新文章",
    )
    entry_writer = models.CharField(
        max_length=100,
        verbose_name="文章作者",
        default="佚名",
    )
    entry_time = models.DateTimeField(
        verbose_name="发布日期",
        auto_now_add=True,
    )
    entry_content = models.TextField(
        verbose_name="文章内容",
        default=""
    )
    entry_label = models.SlugField(
        max_length=100,
        verbose_name="文章标签",
        unique=True,
        help_text="用于URL的英文标识（示例：python-tutorial）"
    )

    class Meta:
        verbose_name = "文章条目"
        verbose_name_plural = verbose_name
        ordering = ['-entry_time']  # 按发布时间倒序

    def __str__(self):
        return f"{self.entry_title}（{self.board.board_title}）"

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={
            'board_id': self.board.board_id,
            'entry_label': self.entry_label
        })