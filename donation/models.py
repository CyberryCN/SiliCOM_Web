from django.db import models

# Create your models here.
class Donor(models.Model):
    donation_time = models.DateTimeField(  # 改为时间字段
        verbose_name="捐赠时间"
    )
    donor_name = models.CharField(
        verbose_name="捐赠人",
        max_length=100,
        default="佚名",
    )
    donation_worth = models.FloatField(
        verbose_name="捐赠金额",
        default=0,
    )
    donation_object = models.CharField(
        verbose_name="捐赠物品",
        max_length=100,
    )
    donation_id = models.AutoField(
        verbose_name="捐赠编号",
        primary_key=True,
    )

    def __str__(self):
        return self.donor_name