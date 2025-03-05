# service/forms.py
from django import forms
from .models import Sign, Comment
from django.core.validators import MinValueValidator, MaxValueValidator

class SignupForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['nick_name', 'machine', 'requirement', 'phone_number']  # 添加昵称字段
        labels = {
            'nick_name': '显示昵称',
            'machine': '设备型号',
            'requirement': '具体需求',
            'phone_number': '联系电话'
        }
        help_texts = {
            'nick_name': '将在评价中显示的名称（如：小明同学）'
        }

class CommentForm(forms.Form):
    unique_code = forms.CharField(
        label='识别码',
        max_length=36,
        widget=forms.TextInput(attrs={'placeholder': '请输入12位识别码'})
    )
    rating = forms.IntegerField(
        label='服务评分',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 5}),
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    content = forms.CharField(
        label='评价内容',
        widget=forms.Textarea(attrs={'rows': 4})
    )
