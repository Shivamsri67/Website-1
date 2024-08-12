from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import itemform
from django.http import Http404
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    item_list=item.objects.all()
    # return HttpResponse(item_list)
    temp=loader.get_template('food/index.html')
    context={'item_list':item_list,}
    return HttpResponse(temp.render(context,request))
@login_required
def detail(request,pk):
    obj=item.objects.get(id=pk)
    return render(request,'food/detail.html',{'obj':obj})

def home(request):
    return render(request,'food/home.html')
@login_required
def add_item(request):
    form=itemform(request.POST or None)
    if form.is_valid():
        form.save()
        # name=form.cleaned_data.get('name')
        # desc=form.cleaned_data.get('desc')
        # price=form.cleaned_data.get('price')
        # image=form.cleaned_data.get('image')
        # item.objects.create(name=name,desc=desc,price=price,image=image)


        return redirect('food:index')

    
    return render(request,'food/item_form.html',{'form':form})
@login_required
def edit_item(request,pk):
    insta=item.objects.get(id=pk)
    form=itemform(request.POST or None,instance=insta)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'insta':insta})
@login_required
def delete_item(request,pk):
    insta=item.objects.get(id=pk)
    if request.method=='POST':
        insta.delete()
        return redirect('food:index')
    return render(request,'food/item_delete.html',{'insta':insta})