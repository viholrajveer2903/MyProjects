from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='indent'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
     path('login1/',views.login1,name='login1'),
    ]