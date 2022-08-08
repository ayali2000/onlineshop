from django.shortcuts import redirect, render
from django.contrib import messages
from store.forms import OrederForm, SellForm
from . models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    all_prods = Items.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = all_prods
        context = {'all_prods':all_prods,
                'query':query,
                'queryset':queryset,
                'result':result}
    return render(request,'store/index.html',context)

def detail(request,pk):
    item = Items.objects.get(pk=pk)
    Ord_Form = OrederForm()
    if request.method == "POST":
        Ord_Form = OrederForm(request.POST)
        if Ord_Form.is_valid():
            instance = Ord_Form.save(commit=False)
            instance.Product_name = item.Name
            instance.save()
            return redirect('detail')
        else:
            Ord_Form = OrederForm()
    context = {
        'Ord_Form':Ord_Form,
        'item':item
    }
    return render(request,'store/detail.html',context)
    

@login_required
def sell(request):
    frm = SellForm()
    if request.method == "POST":
        frm = SellForm(request.POST)
        if frm.is_valid():
            frm.save()
            frm.clean()
            messages.success(request,'Item posted')
            return redirect('index')
        else:
            frm = SellForm()
    context = {'frm':frm}    
    return render(request,'store/sell.html',context)    

def phone(request):
    cat_prods = Items.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = cat_prods
    context = {'cat_prods':cat_prods,
               'query':query,
               'queryset':queryset,
               'cat_prods':cat_prods,
               'result':result
               }

    return render(request,'store/phone.html',context)
