from django.shortcuts import render, redirect
from django.urls import reverse

from cafe.models import Menu
from cafe.forms import CommentForm

# Create your views here.

def menu_detail(request, post_id): 

    menu = Menu.objects.get(id = post_id)
    comment_form = CommentForm()

    context = {
        "menu" : menu, 
        "comment_form" : comment_form,
    }

    return render(request, "menu_detail.html", context)

def post_like(request, post_id) : 
    menu = Menu.objects.get(id = post_id)
    user = request.user # 좋아요 한 사람

    user.like_menu.add(menu)

    # 왼쪽이 True or 오른쪽이 False
    url = reverse("cafe:detail") 
    return redirect(url)
