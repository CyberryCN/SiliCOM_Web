from django.shortcuts import render
from .models import Operator

# Create your views here.
def index(request):
    # 社团历史内容（留空部分）
    context = {
        'history': """
                <p>（在此填写社团历史文字内容）</p>
                <p>示例内容：SiliCOM电脑协会成立于2005年，致力于...</p>
            """,
        'operators': Operator.objects.all().order_by('op_id')
    }
    return render(request, 'introduction/index.html', context)