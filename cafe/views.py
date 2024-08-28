from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

from users.models import Like
from cafe.models import Menu, Comment
from cafe.forms import CommentForm

# Create your views here.

def menu_detail(request, menu_id): 

    menu = Menu.objects.get(id = menu_id)
    comment_form = CommentForm()

    context = {
        "menu" : menu, 
        "comment_form" : comment_form,
    }

    if request.method == "POST": 
        comment_content = request.POST["comment"]

    return render(request, "menu_detail.html", context)

@require_POST
def menu_like(request, menu_id) : 
    menu = Menu.objects.get(id = menu_id)    
    user = request.user # 좋아요 한 사람

    if request.method == "POST": 
        if Like.objects.filter(menu_id=menu_id, user_id=user.id).exists():
            Like.objects.filter(menu_id=menu_id, user_id=user.id).delete()

        else: 
            Like.objects.create(
                menu_id = menu, 
                user_id = user,
            )

        return redirect("cafe:detail") 




@require_POST
def comment_delete(request, comment_id): 
    comment = Comment.objects.get(id=comment_id)

    if comment.user == request.user: 
        comment.delete()

        url = reverse("posts:feeds") + f"#post-{comment.post.id}"
        return redirect(url)
    
    else: 
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")
 


# Create your views here.
def main(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        category = request.POST.get("category")
        order_by = request.POST.get("order_by")

        if brand == "기본" and category == "기본":
            menus = Menu.objects.all()
        elif brand == "기본":
            menus = Menu.objects.filter(category=category)    
        elif category == "기본":
            menus = Menu.objects.filter(brand=brand)
        else:
            menus = Menu.objects.filter(brand=brand, category=category)

        if order_by != "기본":
            menus = Menu.objects.order_by(order_by)
    else:
        menus = Menu.objects.all()
    
    context = {
        "menus": menus
    }
    return render(request, "main.html", context)

