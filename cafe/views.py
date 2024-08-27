from django.shortcuts import render
from cafe.models import Menu
# from cafe.forms import CommentForm

# Create your views here.

def menu_detail(request, post_id): 
    menu = Menu.objects.get(id = post_id)
    # comment_form = CommentForm()
    context = {
        "menu" : menu, 
        # "comment_form" : comment_form,
    }
    return render(request, "menu_detail.html", context)