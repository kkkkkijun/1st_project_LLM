from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

from cafe.models import Menu, Comment
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

def menu_like(request, post_id) : 
    menu = Menu.objects.get(id = post_id)
    user = request.user # 좋아요 한 사람

    user.like_menu.add(menu)

    # 왼쪽이 True or 오른쪽이 False
    url = reverse("cafe:detail") 
    return redirect(url)

# 파이스타그램 copy
# 댓글 작성을 처리할 View, POST 요청만 허용 
@require_POST
def comment_add(request): 
    # request.POST 로 전달된 데이터를 사용해 CommentForm 인스턴스 생성 
    form = CommentForm(data=request.POST)

    if form.is_valid(): 
        # comment=False 옵션으로 메모리상에 Comment 객체 생성 
        comment = form.save(commit=False)

        # Comment 생성에 필요한 사용자 정보를 request 에서 가져와 할당 
        comment.user = request.user

        # DB에 Comment 객체 저장 
        comment.save()

        # 생성된 Comment의 정보 확인 
        print(comment.id)
        print(comment.content)
        print(comment.user_id)

        # URL 로 "next"값을 전달받았다면 댓글 작성 완료 후 전달받은 값으로 이동 
        # if request.GET.get("next"): 
        #     url_next = request.GET.get("next")

        # # "next" 값을 전달받지 않았다면 피드페이지의 글 위치로 이동 
        # else: 
        #     # 생성한 comment 에서 연결된 post 정보를 가져와서 id값을 이용 
        #     url_next = reverse("posts:feeds") + f"#post-{comment.post.id}"
        
        # return redirect(url_next)
    
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
            menus = Menu.order_by(order_by)
    else:
        menus = Menu.objects.all()
    
    context = {
        "menus": menus
    }
    return render(request, "main.html", context)

