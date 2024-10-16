"""
URL configuration for Events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import include
from eventapp import views

app_name = 'eventapp'

urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('events/',include('eventapp.urls')),
# ]

# from django.urls import path
# from . import views

# app_name = 'eventapp'  # Add this line to define the namespace

    path('admin/', admin.site.urls),
    path('events/',include('eventapp.urls')),
    path('', views.index, name='index'),
    path('home/', views.user_home, name='user_home'),
    path('event/', views.user_event, name='user_event'),
    path('booking/', views.event_booking, name='event_booking'),
    path('logout/', views.user_logout, name='user_logout'),
    path('test/', views.test, name='test'),
    path('login_user/', views.login_user, name='login_user'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_booking/', views.admin_booking, name='admin_booking'),
    path('admin_event/', views.admin_event, name='admin_event'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),
    path('add_event/', views.add_event, name='add_event'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('db__booking/', views.db_events_booking, name='db_ground_booking'),
    path('db_update_event/<int:id>/', views.db_update_event, name='db_update_event'),
    path('db_delete_event/<int:id>/', views.db_delete_event, name='db_delete_event'),
    path('db_add_event/', views.db_add_event, name='db_add_event'),
]

