# service/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity, Sign, Comment
from .forms import SignupForm, CommentForm


def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'service/activity_list.html', {
        'activities': activities
    })


def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'service/activity_detail.html', {
        'activity': activity
    })


def signup_view(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    if not activity.available:
        return redirect('activity-detail', activity_id=activity_id)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            sign = form.save(commit=False)
            sign.activity = activity
            sign.save()
            return render(request, 'service/signup_success.html', {
                'unique_code': sign.unique_code,
                'activity': activity,
            })
    else:
        form = SignupForm()

    return render(request, 'service/signup_form.html', {
        'form': form,
        'activity': activity,
    })


def comment_create(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            unique_code = form.cleaned_data['unique_code']
            try:
                sign = Sign.objects.get(unique_code=unique_code)
                Comment.objects.create(
                    activity=activity,
                    sign=sign,
                    rating=form.cleaned_data['rating'],
                    content=form.cleaned_data['content']
                )
                return redirect('service:comment-list', activity_id=activity_id)
            except Sign.DoesNotExist:
                form.add_error('unique_code', '无效的识别码')
    else:
        form = CommentForm()

    return render(request, 'service/comment_form.html', {
        'form': form,
        'activity': activity
    })


def comment_list(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    comments = activity.comments.all()
    return render(request, 'service/comment_list.html', {
        'activity': activity,
        'comments': comments
    })