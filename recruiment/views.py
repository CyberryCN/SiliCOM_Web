from django.shortcuts import render
from .models import RecruitmentDoc

# Create your views here.
def index(request):
    latest_doc = RecruitmentDoc.objects.order_by('-doc_id').first()  # 注意负号表示降序排列
    context = {
        'text':"""
            <p>(在此填写忽悠人来招新的文字)</p>
        """,
        'document':latest_doc,
    }
    return render(request, 'recruitment/index.html', context)