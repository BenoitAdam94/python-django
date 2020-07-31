from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<int:id_article>', views.view_article),
    # path('articles/<str:tag>', views.list_articles_by_tag), 
    # path('articles/<int:year>/<int:month>', views.list_articles),  
    path('redirection', views.view_redirection),
]
