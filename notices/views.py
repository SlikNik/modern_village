from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from notices.models import Notice
from notices.forms import AddNoticeForm

def index_view(request):
    return render(request, 'index.html', {'data': Notice.objects.all().order_by('-post_date')})

def notice_sorted_view(request):
    return render(request, 'index.html', {'newdata': Notice.objects.filter(is_urgent=True), 'olddata': Notice.objects.filter(is_urgent=False)})

def notice_detail(request, id):
    current_notice = Notice.objects.filter(id=id).first()
    return render(request, 'notice_detail.html', {'data': current_notice})

@login_required
def owner_notice_view(request):
    return render(request, 'index.html', {"data": Notice.objects.filter(created_by= request.user)})

@login_required
def add_notice(request):
    if request.method == "POST":
        form = AddNoticeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_notice = Notice.objects.create(
                type_of=data.get('type_of'),
                title=data.get('title'),
                body=data.get('body'),
                price=data.get('price'),
                is_urgent = data.get('is_urgent'),
                creator=request.user
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddNoticeForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def notice_edit(request, id):
    current_notice = Notice.objects.get(id=id)
    if request.method == 'POST':
        form = AddNoticeForm(request.POST)
        if form.is_valid():
            new_notice = form.cleaned_data
            current_notice.type_of = new_notice['type_of']
            current_notice.title = new_notice['title']
            current_notice.body = new_notice['body']
            current_notice.price = new_notice['price']
            current_notice.is_urgent = new_notice['is_urgent']
            current_notice.save()
        return HttpResponseRedirect(reverse('noticedetails', args=[current_notice.id]))
    form = AddNoticeForm(initial={'title' : current_notice.title, 'body': current_notice.body, 
                         'price': current_notice.price, 'type_of': current_notice.type_of, 'is_urgent': current_notice.is_urgent})
    return render(request, 'generic_form.html', {'form': form})