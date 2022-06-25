from django.shortcuts import render
from django.shortcuts import redirect
from account.models import User
from . import models
from . import forms

# Create your views here.
# 必須機能
def index(request):
    search_form = forms.SearchForm(request.GET)
    return render(request, "shopping/main.html",locals())

# def remove_from_cart(request,item_id):
# 任意機能

# def remove_from_cart_commit(request):
# 任意機能

# def purchase(request):
# 任意機能

# def purchase_commit(request):
# 任意機能

# def purchase_history(request):
# 任意機能

# def purchase_cancel(request,purchase_id):
# 任意機能

# def purchase_cancel_commit(request):
# 任意機能
