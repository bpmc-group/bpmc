from django.urls import path
from .views import user_login, user_logout, home_view, info_view, news_view

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home_view, name='home'),
    path('info/', info_view, name='info'),
    path('news/', news_view, name='news'),
]
