from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from notices.models import Notice
from notices.forms import AddNoticeForm
import datetime


class NoticesView(LoginRequiredMixin, TemplateView):
    def get(self, request, notice_type):
        if notice_type == 'URGENT':
            items = Notice.objects.filter(
                is_urgent=True).order_by('-post_date')
        elif notice_type == 'ALL':
            items = Notice.objects.filter(post_date__lte=datetime.datetime.today(
            ), post_date__gt=datetime.datetime.today()-datetime.timedelta(days=30)).order_by('-post_date')
        else:
            items = Notice.objects.filter(post_date__lte=datetime.datetime.today(
            ), post_date__gt=datetime.datetime.today()-datetime.timedelta(days=30)).order_by('-post_date').filter(type_of=notice_type)
        return render(request, 'notices.html', {'form': AddNoticeForm(), 'data': items})

    def post(self, request):
        form = AddNoticeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            breakpoint()
            Notice.objects.create(
                type_of=data.get('type_of'),
                title=data.get('title'),
                body=data.get('body'),
                price=data.get('price'),
                is_urgent=data.get('is_urgent'),
                notice_pic=data.get('notice_pic'),
                creator=request.user
            )
            return HttpResponseRedirect(reverse('allnotices'))
        form = AddNoticeForm()
        return render(request, 'notices.html', {'form': form, 'data': Notice.objects.all().order_by('-post_date')})


def notice_detail(request, id):
    current_notice = Notice.objects.filter(id=id).first()
    return render(request, 'notice_detail.html', {'notice': current_notice})

# @login_required
# def owner_notice_view(request):
#     return render(request, 'index.html', {"data": Notice.objects.filter(created_by= request.user)})

# @login_required
# def add_notice(request):
#     if request.method == "POST":
#         form = AddNoticeForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_notice = Notice.objects.create(
#                 type_of=data.get('type_of'),
#                 title=data.get('title'),
#                 body=data.get('body'),
#                 price=data.get('price'),
#                 is_urgent = data.get('is_urgent'),
#                 creator=request.user
#             )
#             return HttpResponseRedirect(reverse('allnotices'))
#     form = AddNoticeForm()
#     return render(request, 'generic_form.html', {'form': form})


@login_required
def notice_edit(request, id):
    current_notice = Notice.objects.get(id=id)
    if request.method == 'POST':
        form = AddNoticeForm(request.POST, request.FILES)
        if form.is_valid():
            new_notice = form.cleaned_data
            current_notice.type_of = new_notice['type_of']
            current_notice.title = new_notice['title']
            current_notice.body = new_notice['body']
            current_notice.notice_pic = new_notice['notice_pic']
            current_notice.price = new_notice['price']
            current_notice.is_urgent = new_notice['is_urgent']
            current_notice.save()
        return HttpResponseRedirect(reverse('noticedetails', args=[current_notice.id]))
    form = AddNoticeForm(initial={'title': current_notice.title, 'body': current_notice.body, 'notice_pic': current_notice.notice_pic,
                                  'price': current_notice.price, 'type_of': current_notice.type_of, 'is_urgent': current_notice.is_urgent})
    return render(request, 'generic_form.html', {'form': form, 'Type': 'Editing Notice!'})


@login_required
def notice_delete(request, id):
    current_notice = Notice.objects.get(id=id)
    if request.user == current_notice.creator:
        current_notice.delete()
    return HttpResponseRedirect(reverse('allnotices'))
