from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from material.models import Material
from order.models import Receive
from accounts.models import User
from django.shortcuts import redirect
from django.contrib.messages import success


def employee(request):
    if request.method == 'POST':
        form = request.POST
        for name, quantity in form.items():
            if name != 'csrfmiddlewaretoken':
                item = Receive(name=name, quantity=quantity, order_by=request.user, status='pending')
                item.save()
        success(request, 'the Item was successfully send ')
        return redirect('user_area')
    return render(request, 'UserArea.html', {'items': Material.objects.all()})


def admin(request):
    data = Receive.objects.filter(status='pending').order_by('order_by_id')
    context = {'data':data}

    if request.method == 'POST':
        form = request.POST
        for name, quantity in form.items():
            if name != 'csrfmiddlewaretoken':
                print(f"{name}  {quantity}")
        success(request, 'the Item was successfully send ')
        return redirect('user_area')
    return render(request, 'UserArea.html', context=context)


@login_required()
def user_area(request):
    if request.user.groups.filter(name='Employee').exists():
        return employee(request)
    elif request.user.groups.filter(name='Admin').exists():
        return admin(request)


class Home(TemplateView):
    template_name = "index.html"
