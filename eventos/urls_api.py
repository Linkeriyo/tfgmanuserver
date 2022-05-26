from django.urls import path
from eventos import views_api

urlpatterns = [
    # API
    path('get_articles/', views_api.get_articles),
    path('get_favorite_articles/', views_api.get_favorite_articles),
    path('get_remind_me_articles/', views_api.get_remind_me_articles),
    path('get_article/', views_api.get_article),
    path('add_favorite_article/', views_api.add_favorite_article),
    path('remove_favorite_article/', views_api.remove_favorite_article),
]