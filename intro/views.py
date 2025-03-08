from django.shortcuts import render
from .models import Operator

# Create your views here.
def index(request):
    # 社团历史内容（留空部分）
    context = {
        'history': """
                <p>SiliCOM 电脑协会是东南大学成立最早的校级电脑社团之一。
        前身是2015年成立的东南大学本本团，后因形势变化，2019年转型为社团。
        协会承担了全校范围的电脑故障维修、电脑技术宣传、信息技术培训等工作。
        每年通过讲座、义诊和在线答疑等形式服务数千师生。
        经过多年发展协会已经成为软硬技术兼顾、注重社员能力发展、人员结构合理的综合学术科技类社团。</p>
            """,
        'operators': Operator.objects.all().order_by('op_id')
    }
    return render(request, 'introduction/index.html', context)