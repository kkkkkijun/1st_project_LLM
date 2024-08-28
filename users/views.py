from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout

from users.forms import PostForm, LoginForm, SignupForm
from users.models import Post, User

# Create your views here.

# 건의사항 페이지
def feedback(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user_id = request.user
            feedback.save()
    else:
        form = PostForm()

    feedbacks = Post.objects.all()
    context = {
        "feedbacks": feedbacks,
        "form" : form,
    }
    return render(request, "feedback.html", context)

# 건의사항 삭제
def feedback_delete(request, feedback_id):
    Post.objects.filter(id=feedback_id).delete()
    return redirect("users:feedback")

# 건의사항 수정
def feedback_edit(request, feedback_id):
    feedback = get_object_or_404(Post, id = feedback_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=feedback)
        if form.is_valid():
            feedback = form.save(commit = False)
            feedback.save()
            return redirect("users:feedback")
        
    else:
        form = PostForm(instance = feedback) # 수정 대상이 될 데이터를 설정
    return render(request, "feedback_edit.html", {"form" : form})

def login_view(request):
    # 이미 로그인되어 있는 경우
    if request.user.is_authenticated:
        return redirect("cafe:main")
    
    if request.method == "POST":
        # LoginForm 인스턴스를 만들며, 입력 데이터는 request.POST 를 사용
        form = LoginForm(data=request.POST)

        # # LoginForm 에 들어온 데이터가 적절한지 유효성 검사
        # print("form.is_valid():", form.is_valid())

        # # 유효성 검사 이후에는 cleaned_data 에서 데이터를 가져와 사용
        # print("form.cleaned_data:", form.cleaned_data)

        # LoginForm 에 전달된 데이터가 유효하다면
        if form.is_valid():
            # username과 password 값을 가져와 변수에 할당
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # username, password 에 해당하는 사용자가 있는지 검사
            user = authenticate(username=username, password=password)

            # 해당 사용자가 존재한다면
            if user:
                # 로그인 처리 후, 메인 페이지로 redirect
                login(request, user)
                return redirect("cafe:main")

            # 해당 사용자가 없다면 form에 에러 추가
            else:
                form.add_error(None, "해당하는 사용자가 없습니다")

        # 어떤 이유든, 실패한 경우라면 다시 LoginForm 을 사용한 로그인 페이지 렌더링
        context = {
            "form": form,
        }
        return render(request, "login.html", context)

    else:
        form = LoginForm()

        context = {
            "form": form,
        }
        return render(request, "login.html", context)
    
def logout_view(request):
    # logout 함수 호출에 request를 전달
    logout(request)

    # logout 처리 후, 로그인페이지로 이동
    return redirect("users:login")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)

        # Form에 에러가 없다면 form의 save() 메서드로 사용자를 생성
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:login")
    
    # GET 요청에서는 빈 Form을 보여줌
    else:
        # SignupForm 인스턴스를 생성, Template에 전달
        form = SignupForm()

    # context로 전달되는 form 은 두 가지 경우가 존재
    # 1. POST 요청에서 생성된 form 이 유효하지 않은 경우
    # --> 에러를 포함한 form이 사용자에게 보여짐
    # 2. GET 요청으로 빈 form이 생성된 경우
    # --> 빈 form이 사용자에게 보여짐
    context = {"form" : form}
    return render(request, "signup.html", context)