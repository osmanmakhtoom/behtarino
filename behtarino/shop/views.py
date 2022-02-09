from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Category, Product, Order, OrderLine


def index(request):
    pass
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'shop/index.html', context)
