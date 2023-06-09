# """user_log URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from user.views import home_view
# from django.contrib.auth import views as auth_views
# from user.views import home_view

# from user import views as user_views
# # app_name = 'auth'
# from user.views import home_view, login_view
# from user import views as user_views
# from user.views import home_view, login

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home_view, name='home'),
#     path('login/', login_view, name='login'),
#     path('register/', user_views.register, name='register'),
# ]
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     # path(' ', home_view, name='home'),
# #     path('register/', user_views.register, name='register'),
# #     path('login/', views.login_view, name='login'),

# # ]


from django.contrib import admin
from django.urls import path
from user.views import home_view, login_view, register
from django.contrib.auth import views as auth_views
from django.urls import path
# from .views import user_profile_view
# from user_log.views import user_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('user-profiles/', user_profile_view, name='user_profiles'),

]
