from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from users.models import Like, User
from cafe.models import Menu
from cafe.forms import CommentForm, LikeForm

# Create your views here.

def menu_detail(request, post_id): 

    menu = Menu.objects.get(id = post_id)
    comment_form = CommentForm()
    like_form = LikeForm()

    context = {
        "menu" : menu, 
        "comment_form" : comment_form,
        "like_form" : like_form,
    }

    return render(request, "menu_detail.html", context)

@login_required
def menu_like(request, post_id): 
    menu = get_object_or_404(Menu, id=post_id)
    user = request.user

    existing_like = Like.objects.filter(menu=menu, user=user).first()

    if existing_like:
        # 좋아요가 이미 있다면 제거
        existing_like.delete()
    else:
        # 좋아요가 없다면 추가
        Like.objects.create(menu=menu, user=user)

    # 좋아요가 적용된 메뉴 페이지로 리디렉션
    return redirect("cafe:detail")
