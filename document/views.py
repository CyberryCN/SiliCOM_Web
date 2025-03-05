from django.shortcuts import render, get_object_or_404
from .models import Board, Entry

# Create your views here.
def board_list(request):
    """展示所有板块"""
    boards = Board.objects.all()
    return render(request, 'document/board_list.html', {'boards': boards})

def board_detail(request, board_id):
    """展示指定板块下的所有文章"""
    board = get_object_or_404(Board, board_id=board_id)
    entries = board.entries.all()
    return render(request, 'document/board_detail.html', {
        'board': board,
        'entries': entries
    })

def entry_detail(request, board_id, entry_label):
    """展示文章详情"""
    entry = get_object_or_404(
        Entry,
        board__board_id=board_id,
        entry_label=entry_label
    )
    return render(request, 'document/entry_detail.html', {'entry': entry})
