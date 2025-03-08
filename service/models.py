import uuid
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Activity(models.Model):
    activity_id = models.AutoField(  # 改为自动递增主键
        primary_key=True,
        verbose_name="活动编号",
        help_text="活动唯一标识符"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="活动名称"
    )
    activity_time = models.DateTimeField(  # 改为时间字段
        verbose_name="活动时间"
    )
    limit_time = models.DateTimeField(  # 改为时间字段
        verbose_name="报名截止时间"
    )
    available = models.BooleanField(
        default=True,
        verbose_name="报名开放状态"
    )

    def __str__(self):
        return f"{self.title}（ID：{self.activity_id}）"

    def save(self, *args, **kwargs):
        """自动更新报名状态"""
        now = timezone.now()
        if now > self.limit_time:
            self.available = False
        else:
            self.available = True
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "活动列表"
        ordering = ['-activity_time']

class Sign(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='signups'
    )
    unique_code = models.UUIDField(  # 唯一识别码
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    machine = models.CharField(
        max_length=100,
        verbose_name="电脑型号",
        help_text="例如：联想拯救者Y7000 2023款"
    )
    nick_name = models.CharField(  # 新增昵称字段
        max_length=50,
        verbose_name="用户昵称",
        help_text="将在评价中显示的名称",
        default="匿名用户"
    )
    requirement = models.TextField(
        verbose_name="具体需求"
    )
    phone_number = models.CharField(  # 改为字符串类型
        max_length=20,
        verbose_name="联系电话",
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')]
    )
    sign_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="报名时间"
    )

    def __str__(self):
        return f"{self.activity.title} - {self.unique_code}"

    class Meta:
        verbose_name_plural = "报名记录"
        ordering = ['-sign_time']

class Comment(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    sign = models.ForeignKey(
        Sign,
        on_delete=models.CASCADE,
        related_name='comments',  # 保留反向关联
        verbose_name='关联报名'  # 可选：添加注释
        # 移除 unique=True
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="服务评分"
    )
    content = models.TextField(
        verbose_name="评价内容"
    )
    comment_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="评价时间"
    )

    class Meta:
        verbose_name_plural = "用户评价"
        ordering = ['-comment_time']

    def __str__(self):
        return f"{self.sign.unique_code}的评价"

    def get_display_info(self):
        """获取需要展示的报名信息"""
        return {
            'nickname': self.sign.nick_name,
            'machine': self.sign.machine,
            'requirement': self.sign.requirement
        }