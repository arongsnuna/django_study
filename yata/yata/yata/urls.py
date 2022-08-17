from django.contrib import admin
from django.urls import path, include
from yataapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),

    path('roomcreate/', views.roomcreate, name='roomcreate'),
    path('detail/<int:room_id>', views.detail, name='detail'),
]
