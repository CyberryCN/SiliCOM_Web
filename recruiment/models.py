from django.db import models
import os

# Create your models here.
class RecruitmentDoc(models.Model):
    document = models.FileField(
        upload_to='recruitment_docs',
        verbose_name="招新报表",
        blank=True,
    )
    doc_label = models.CharField(
        max_length=100,
        verbose_name="文件名"
    )
    doc_id = models.AutoField(
        primary_key=True,
        verbose_name="文件编号",
    )


    @property
    def doc_path(self):
        if self.document:
            return self.document.url
        return f'/static/recruitment/document/recruitment.docx'

    def save(self, *args, **kwargs):
        """自动重命名上传的文档"""
        if self.document and not self.document.name.startswith(f'operator_{self.doc_label}'):
            # 获取文件扩展名
            ext = os.path.splitext(self.document.name)[1]
            # 生成新文件名
            self.document.verbose_name = f'operator_{self.doc_label}{ext}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.doc_path