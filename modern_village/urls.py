"""modern_village URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from modern_users import views as modernusersviews
from post import views as postviews
from notices import views as noticeviews
from authentication import views as authenticateviews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
"""Not for production level"""
"""Not for production level"""


handler404 = modernusersviews.handler404
handler500 = modernusersviews.handler500

urlpatterns = [
    path('', modernusersviews.index_view, name="homepage"),
    path('notice/<int:id>/delete/', noticeviews.notice_delete, name='editnotice'),
    path('notice/<int:id>/edit/', noticeviews.notice_edit, name='editnotice'),
    path('notice/<int:id>/', noticeviews.notice_detail, name='noticedetails'),
    path('notices/<str:notice_type>/',
         noticeviews.NoticesView.as_view(), name='notices'),
    path('posts/<int:post_id>/', postviews.PostReplyView.as_view(), name='postreply'),
    path('posts/<int:post_id>/edit/', postviews.post_edit_view),
    path('posts/<int:post_id>/del/', postviews.post_delete_view),
    path('posts/', postviews.PostView.as_view(), name='chat'),
    path('follow/<int:user_id>/', modernusersviews.follow_view, name='follow'),
    path('unfollow/<int:user_id>/', modernusersviews.unfollow_view, name='unfollow'),
    path('profile/<str:username>/delete/', modernusersviews.profile_delete, name='deleteprofile'),
    path('profile/<str:username>/edit/', modernusersviews.profile_edit, name='editprofile'),
    path('profile/<str:username>/', modernusersviews.profile_view, name='profileview'),
    path('signup/', modernusersviews.sign_up_view, name="signupview"),
    path('login/', authenticateviews.login_view, name="loginview"),
    path('logout/', authenticateviews.logout_view, name="logoutview"),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
