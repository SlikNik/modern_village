from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from modern_users.models import ModernUsers
from modern_users.forms import SignUpForm, EditProfileForm
from notices.models import Notice
from post.models import Post


def index_view(request):
    return render(request, 'index.html')


def profile_view(request, username):
    current_user = ModernUsers.objects.filter(username=username).first()
    notices = Notice.objects.filter(
        creator=current_user).order_by('-post_date')
    posts = Post.objects.filter(creator=current_user).order_by('-post_date')
    profile = ModernUsers.objects.get(id=current_user.id)
    following = request.user.followers.all()
    following_list = list(following)
    return render(request, 'profile.html', {"current_user": current_user, "notices": notices, "posts": posts, "profile": profile, "user_following": following_list})

@login_required
def follow_view(request, user_id):
    request.user.followers.add(ModernUsers.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("homepage"))


@login_required
def unfollow_view(request, user_id):
    request.user.followers.remove(ModernUsers.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("homepage"))



@login_required
def profile_edit(request, username):
    current_user = ModernUsers.objects.get(username=username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.cleaned_data
            current_user.user_pic = new_user['user_pic']
            current_user.first_name = new_user['first_name']
            current_user.last_name = new_user['last_name']
            current_user.birthday = new_user['birthday']
            current_user.age = new_user['age']
            current_user.address = new_user['address']
            current_user.city = new_user['city']
            current_user.zipcode = new_user['zipcode']
            current_user.facebook = new_user['facebook']
            current_user.twitter = new_user['twitter']
            current_user.instagram = new_user['instagram']
            current_user.user_pic = new_user['user_pic']
            current_user.save()
        return HttpResponseRedirect(reverse('noticedetails', args=[current_user.id]))
    form = EditProfileForm(initial={'first_name': current_user.first_name, 'last_name': current_user.last_name,
                                    'birthday': current_user.birthday, 'age': current_user.age, 'address': current_user.address,
                                    'city': current_user.city, 'zipcode': current_user.zipcode, 'facebook': current_user.facebook,
                                    'twitter': current_user.twitter, 'instagram': current_user.instagram, 'user_pic': current_user.user_pic})
    return render(request, 'generic_form.html', {'form': form, 'Type': 'Updating Profile!'})


@login_required
def profile_delete(request, username):
    current_user = ModernUsers.objects.get(username=username)
    if request.user == current_user:
        current_user.delete()
    return HttpResponseRedirect(reverse('homepage'))


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            breakpoint()
            new_user = ModernUsers.objects.create_user(
                user_pic=data.get('user_pic'),
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                birthday=data.get('birthday'),
                age=data.get('age'),
                address=data.get('address'),
                city=data.get('city'),
                zipcode=data.get('zipcode'),
                facebook=data.get('facebook'),
                twitter=data.get('twitter'),
                instagram=data.get('instagram'),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, 'generic_form.html',  {'form': form, 'Type': 'Join the Village!'})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
