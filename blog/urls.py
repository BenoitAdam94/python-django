from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.home),
    path('articles/<int:id_articles>', views.view_articles),
    # path('articles/<str:tag>', views.list_articles_by_tag), 
    # path('articles/<int:year>/<int:month>', views.list_articles),  
    path('redirection', views.view_redirection),
    path('date/', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
