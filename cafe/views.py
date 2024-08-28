from django.shortcuts import render
from cafe.models import Menu

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