from django.urls import path
from . import views
urlpatterns = [
    path('search_restaurant/',views.search_restaurant),
    path('search_open_restaurant/',views.search_open_restaurant),
    path('close_restaurant',views.close_restaurant),
    path('search_idconfig_by_restaurant/',views.search_idconfig_by_restaurant),
    path('change_idconfig/',views.change_idconfig),
    path('change_cache/',views.change_cache),
    path('login/',views.login)
]